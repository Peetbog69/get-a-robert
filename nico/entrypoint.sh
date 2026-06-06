#!/bin/bash
set -e

PROFILE="${HERMES_PROFILE:-default}"
export TELEGRAM_BOT_TOKEN="${TELEGRAM_BOT_TOKEN}"

if [ -z "$TELEGRAM_BOT_TOKEN" ]; then
    echo "ERROR: TELEGRAM_BOT_TOKEN not set"
    exit 1
fi

echo "Starting Hermes gateway for profile: $PROFILE"
mkdir -p /root/.hermes
cp /opt/nico/SOUL.md /root/.hermes/SOUL.md
cp /opt/nico/config.yaml /root/.hermes/config.yaml
rm -f /root/.hermes/auth.json
chmod 600 /root/.hermes/config.yaml
exec hermes --profile "$PROFILE" gateway run --replace
