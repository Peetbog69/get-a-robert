# 🚀 Ampersand Deployment Standard

> **Efficiency · Security · Repeatability**
> Every bot follows the same playbook. No snowflakes.

## 1. Prerequisites

### 1.1 Bot Token
- Create bot via [@BotFather](https://t.me/BotFather)
- Save token to `/opt/ampersand/.env`:
  ```
  BOT_NAME_TOKEN=123456:ABC-DEF…
  ```
  ⚠ Never commit tokens. Never paste in chat. The `.env` file is the single source.

### 1.2 User / Chat ID
- Get the target user's Telegram chat ID (DM the bot once → check logs)
- Document in the env file:
  ```
  BOT_NAME_ALLOWED_USERS=8937417346
  ```

### 1.3 Persona (SOUL.md)
- Write a SOUL.md for the bot
- Place at `bots/<name>/SOUL.md`

## 2. Container Setup

### 2.1 Image
- Base image: `ampersand-bot:latest` (built from `/opt/ampersand/Dockerfile`)
- Contains: Python 3.12-slim, Hermes agent, xz-utils, curl, git, jq
- Entrypoint reads `TELEGRAM_BOT_TOKEN` from the compose env (not hardcoded)
- To rebuild:
  ```bash
  docker build -t ampersand-bot:latest /opt/ampersand/
  ```

### 2.2 Compose Service
Add a service block to `/opt/ampersand/docker-compose.yml`:

```yaml
  bot-name:
    image: ampersand-bot:latest
    container_name: ampersand-<name>
    restart: unless-stopped
    volumes:
      - <name>_data:/root/.hermes
    environment:
      - HERMES_PROFILE=default
      - HERMES_TELEGRAM_BOT_TOKEN=${BOT_NAME_TOKEN}
      - TELEGRAM_BOT_TOKEN=${BOT_NAME_TOKEN}
      - TELEGRAM_ALLOWED_USERS=${BOT_NAME_ALLOWED_USERS}
    mem_limit: 256m
    networks:
      - ampersand-net
```

Add volume declaration:
```yaml
volumes:
  <name>_data:
```

### 2.3 Start
```bash
cd /opt/ampersand && docker compose up -d bot-name
```

## 3. Verification

### 3.1 Health Check
```bash
docker ps --filter name=ampersand-<name>
docker exec ampersand-<name> cat /root/.hermes/gateway_state.json | python3 -m json.tool
```

Expected:
- `gateway_state: running`
- `platforms.telegram.state: connected`

### 3.2 Smoke Test
- DM the bot on Telegram
- Confirm it responds with the correct persona
- Confirm `TELEGRAM_ALLOWED_USERS` blocks unauthorized users (test from a different account)

## 4. Operations

### 4.1 Restart
```bash
docker compose restart <name>
```

### 4.2 Logs
```bash
docker logs ampersand-<name> -n 100
```

### 4.3 Backup
The named volume is your single point of data persistence:
```bash
docker run --rm -v <name>_data:/data -v /backup:/backup alpine tar czf /backup/<name>-$(date +%Y%m%d).tgz /data
```

### 4.4 Teardown
```bash
docker compose down <name>
docker volume rm <name>_data
docker rmi ampersand-bot:latest
```

## 5. Automated Deploy (Goal)
Future state — a CLI that does steps 1–3 in one command:
```bash
create-bot <name> <token> <user-id> <soul-file>
```
Output: running container, verified, ready to talk.
