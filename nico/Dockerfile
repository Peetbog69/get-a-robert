FROM python:3.12-slim

# Install system deps
RUN apt-get update -qq && apt-get install -y -qq curl git jq xz-utils && rm -rf /var/lib/apt/lists/*

# Install Hermes
RUN pip install -q hermes-agent

# Copy entrypoint
COPY SOUL.md /opt/nico/SOUL.md
COPY config.yaml /opt/nico/config.yaml
COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

ENTRYPOINT ["/entrypoint.sh"]
