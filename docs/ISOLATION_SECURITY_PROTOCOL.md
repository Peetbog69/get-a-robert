# 🔒 Ampersand Isolation & Security Protocol

> Every bot is a black box. No cross-talk. No shared state. No exceptions.

## 1. Container Isolation (Hard Boundary)

### 1.1 Mandatory
- [ ] **One container per bot** — no exceptions
- [ ] **Own named volume** (`<name>_data`) — never shared between bots
- [ ] **Own Telegram bot token** — never reused across services
- [ ] **Own config.yaml / .env** — lives inside the volume, scoped to that container

### 1.2 Reasoning
The original sin was a single gateway serving multiple users and bots. That's what caused Tyler to receive Robert's messages in his own DM. Containers + isolated volumes prevent this at the infrastructure level — not configuration, not luck.

## 2. Access Control (Telegram)

### 2.1 User Allowlisting
Every bot MUST set `TELEGRAM_ALLOWED_USERS` to the target user's Telegram chat ID:

```yaml
environment:
  - TELEGRAM_ALLOWED_USERS=8937417346
```

- Only this user can message the bot
- All other DMs are silently rejected
- This prevents accidental discovery, testing from wrong accounts, and cross-talk

### 2.2 No Wildcards
`ALLOW_ALL_USERS=true` is acceptable for dev/test bots on isolated tokens, **never** for production client bots.

## 3. Data Isolation

### 3.1 Volume Boundaries
| Data | Rule |
|------|------|
| Sessions | Per-bot volume only |
| Memories | Per-bot volume only |
| State DB | Per-bot volume only |
| Cron jobs | Per-bot volume only |

### 3.2 No Shared Access
- Bot A cannot read Bot B's volume
- Bot A cannot read Bot B's sessions
- Bot A cannot message Bot B's users

## 4. Secrets Management

### 4.1 What's a Secret
- Telegram bot tokens
- Email passwords
- API keys (OpenAI, DeepSeek, Tavily, Exa, etc.)
- Any credential that grants access to a service or user data

### 4.2 Rules
- [ ] Never hardcode secrets in configs, Dockerfiles, or entrypoints
- [ ] Secrets live in `/opt/ampersand/.env` (chmod 600, root-owned)
- [ ] `.env` files are never committed, pasted, or documented in plaintext
- [ ] Compose references secrets as variables: `${BOT_NAME_TOKEN}`
- [ ] Entrypoint reads from environment, **never** overrides with literals

### 4.3 Rotation
- Rotate tokens when a bot is decommissioned
- Rotate immediately if a secret is exposed (logs, chat, commit)

## 5. Persona Isolation

### 5.1 Each Bot Has Its Own SOUL
- SOUL.md lives in a `bots/<name>/` directory in the repo
- Only one SOUL per container
- No persona mixing, no shared context

### 5.2 Profile System
- Use `HERMES_PROFILE=default` for single-persona bots
- Advanced: separate profiles per persona if multi-gateway, but each still gets its own container

## 6. Network

### 6.1 Bridge Network
All containers join `ampersand-net` for internal communication if needed:
```yaml
networks:
  - ampersand-net
```

### 6.2 No Host Network Mode
Containers share the host's localhost but do not bind external ports. All bot ingress goes through Telegram's API (outbound from the container).

## 7. Monitoring (Goal)

### 7.1 Health State
```bash
docker ps --filter status=running
```
Gateway state is available at `file:///root/.hermes/gateway_state.json` inside each container.

### 7.2 Failure Response
Docker restart policy: `unless-stopped`. If the container fails >5 times in quick succession, investigate — don't just let it cycle.

## 8. Enforcement Checklist (New Bot)

- [ ] New bot token from @BotFather
- [ ] New volume: `docker volume create <name>_data`
- [ ] New compose service (copy robert block, change name + token + user)
- [ ] `TELEGRAM_ALLOWED_USERS` set to the ONE target user
- [ ] Secrets in `.env` only, never in the compose file
- [ ] `docker compose up -d <name>`
- [ ] Verify: gateway_state → telegram connected
- [ ] Verify: unauthorized user is rejected
- [ ] Verify: bot responds only for the authorized user
