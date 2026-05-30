#!/usr/bin/env bash
# 🦞 Cloud Assembly — Trial Bot Deployment Pipeline
# Usage:  ./cloud-assembly.sh <bot-name> <bot-token> <persona-file>
# Example: ./cloud-assembly.sh sage "123:abc" /path/to/sage-soul.md

set -euo pipefail

if [ $# -lt 3 ]; then
  echo "Usage: $0 <bot-name> <bot-token> <persona-file>"
  echo "  bot-name     : human-readable name (e.g., sage)"
  echo "  bot-token    : Telegram bot token from @BotFather"
  echo "  persona-file : path to SOUL.md for this bot"
  exit 1
fi

BOT_NAME="$1"
BOT_TOKEN="$2"
PERSONA_FILE="$3"
HERMES_HOME="/root/.${BOT_NAME}"
HERMES_SRC="/usr/local/lib/hermes-agent"
DEEPSEEK_KEY="sk-b322eff9e837d23371b01dad3167e0a8cbe56416ba0840032"

echo "🧬 Assembling agent: ${BOT_NAME}"

# 1. Create agent home directory
ssh root@vultr-1 "mkdir -p ${HERMES_HOME}"
echo "   ✅ Created ${HERMES_HOME}"

# 2. Copy SOUL.md
scp "$PERSONA_FILE" "root@vultr-1:${HERMES_HOME}/SOUL.md"
echo "   ✅ Loaded persona"

# 3. Deploy .env
ssh root@vultr-1 "cat > ${HERMES_HOME}/.env << 'ENVEOF'
# ${BOT_NAME} - Trial Bot
TELEGRAM_BOT_TOKEN=${BOT_TOKEN}
GATEWAY_ALLOW_ALL_USERS=true
DEEPSEEK_API_KEY=${DEEPSEEK_KEY}
HERMES_DEFAULT_PROVIDER=deepseek
EMAIL_POLL_INTERVAL=30
EMAIL_IMAP_PORT=993
EMAIL_SMTP_PORT=587
ENVEOF"
echo "   ✅ .env written"

# 4. Deploy config.yaml
ssh root@vultr-1 "cat > ${HERMES_HOME}/config.yaml << 'CONFEOF'
model:
  name: deepseek/deepseek-chat
  provider: deepseek
  default: deepseek-v4-flash
  base_url: https://api.deepseek.com/v1
providers: {}
agent:
  max_turns: 90
  gateway_timeout: 1800
  api_max_retries: 3
  image_input_mode: auto
terminal:
  backend: local
  modal_mode: auto
  timeout: 180
  persistent_shell: true
  docker_image: nikolaik/python-nodejs:python3.11-nodejs20
  container_memory: 2048
web:
  search_backend: ddgs
telegram:
  reactions: false
  allowed_chats: '*'
memory:
  memory_enabled: true
  user_profile_enabled: true
  memory_char_limit: 2200
  user_char_limit: 1375
stt:
  enabled: true
  provider: local
tts:
  provider: edge
  edge:
    voice: en-US-AriaNeural
voice:
  auto_tts: true
display:
  personality: default
honcho: {}
logging:
  level: INFO
  max_size_mb: 5
  backup_count: 3
sessions:
  auto_prune: false
  retention_days: 7
approvals:
  mode: auto
security:
  redact_secrets: true
_context_version: 23
CONFEOF"
echo "   ✅ config.yaml written"

# 5. Create systemd service
ssh root@vultr-1 "cat > /etc/systemd/system/${BOT_NAME}-gateway.service << 'SERVICEEOF'
[Unit]
Description=${BOT_NAME} - Trial Bot Gateway
After=network-online.target
Wants=network-online.target
StartLimitIntervalSec=0

[Service]
Type=simple
User=root
Group=root
ExecStart=${HERMES_SRC}/venv/bin/python -m hermes_cli.main gateway run --replace
WorkingDirectory=${HERMES_SRC}
Environment='HOME=/root'
Environment='USER=root'
Environment='HERMES_HOME=${HERMES_HOME}'
Environment='PATH=${HERMES_SRC}/venv/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin'
Environment='VIRTUAL_ENV=${HERMES_SRC}/venv'
Restart=always
RestartSec=5
KillMode=mixed
KillSignal=SIGTERM
TimeoutStopSec=210
StandardOutput=journal
StandardError=journal

[Install]
WantedBy=multi-user.target
SERVICEEOF"
echo "   ✅ systemd service created"

# 6. Register and start
ssh root@vultr-1 "systemctl daemon-reload && systemctl enable ${BOT_NAME}-gateway.service && systemctl start ${BOT_NAME}-gateway.service"
echo "   ✅ Service started"

echo ""
echo "🎉 ${BOT_NAME} is live!"
echo "   DM @<bot-username> on Telegram to test."
echo "   Logs: journalctl -u ${BOT_NAME}-gateway.service -f"
