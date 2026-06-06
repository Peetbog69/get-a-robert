# Bot Intake Checklist

> For every new bot/client/tester. The goal: **efficiency, security, repeatability**.

## 1. Required Inputs
- [ ] Bot name
- [ ] Owner / client name
- [ ] Telegram bot token
- [ ] Target Telegram chat/user ID
- [ ] Persona / purpose summary
- [ ] Any special tools needed (email, web, vision, etc.)

## 2. Safety / Scope
- [ ] Confirm bot is isolated (one container, one volume, one token)
- [ ] Confirm allowed users list
- [ ] Confirm no shared memory/session with other bots
- [ ] Confirm secrets handling method

## 3. Soul / Persona (separate step)
- [ ] Tone / vibe
- [ ] Boundaries
- [ ] What it should never do
- [ ] Greeting style
- [ ] Memory behavior
- [ ] Emoji / style preferences

## 4. Deployment
- [ ] Add compose service
- [ ] Add volume
- [ ] Add token env vars
- [ ] Add allowed users env var
- [ ] Add SOUL.md / persona file
- [ ] Build or reuse image
- [ ] Start container

## 5. Verification
- [ ] Container running
- [ ] `gateway_state.json` shows running
- [ ] Telegram connected
- [ ] Authorized user can message bot
- [ ] Unauthorized user is blocked
- [ ] Bot responds in correct voice

## 6. Backup / Recovery
- [ ] First backup after deployment
- [ ] Confirm state.db and sessions are included
- [ ] Confirm restore path documented

## 7. Handoff
- [ ] Record bot name, token source, user ID, and container name
- [ ] Record any special config decisions
- [ ] Record next maintenance step

## 8. Optional Later
- [ ] Health check script
- [ ] Backup script
- [ ] Monitoring/alerts
- [ ] Rotation / decommission plan

---

**Rule:** if the bot isn’t isolated, it isn’t done.
