FROM node:22-bookworm-slim

RUN apt-get update && apt-get install -y --no-install-recommends \
    ca-certificates \
    curl \
    chromium \
    chromium-common \
    chromium-sandbox \
    && rm -rf /var/lib/apt/lists/*

RUN ln -s /usr/bin/chromium /usr/bin/brave 2>/dev/null || true

ENV CHROMIUM_PATH=/usr/bin/chromium

RUN groupadd -g 1000 gravy && useradd -m -u 1000 -g 1000 gravy
USER gravy
WORKDIR /home/gravy/.openclaw

ENTRYPOINT ["node", "/home/gravy/.npm-global/lib/node_modules/openclaw/dist/index.js", "gateway", "--port", "18789"]
