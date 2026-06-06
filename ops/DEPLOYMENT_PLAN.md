# Robert — Deployment Plan (Hermes Architecture)
**Updated: June 6, 2026**

---

## The Architecture

VPS runs Hermes Agent with a single Telegram bot token. The gateway multiplexes by user ID — each profile has its own `allowed_chats`, SOUL, skills, and memories. No separate bot instances needed.

```
User → Telegram → Hermes Gateway → Profile (Robert)
                         ↓
                  allowed_chats match?
                  Yes → Robert responds
                  No  → ignored
```

---

## Current State

- **Robert** — running on VPS (216.128.154.45), profile `robert`
- **Melissa** — active user, her Telegram ID locked in `allowed_chats`
- **Gateway** — `hermes-gateway.service`, routes by user ID

---

## How It Works

### Telegram Gateway Routing
1. User messages the Hermes Telegram bot
2. Gateway checks the sender's Telegram ID
3. Routes to the matching profile via `allowed_chats` in that profile's config
4. Profile's SOUL.md + system prompt handles the response

### Profile Isolation
- Each profile has its own config, SOUL, skills, memories
- Profiles run in parallel under the same Hermes instance
- No cross-contamination between users

### No Separate Tokens
- One Hermes Telegram bot token serves all profiles
- Cleaner than separate bot instances per user

---

## Adding a New User (When Ready)

1. Create profile: `hermes profile create <name>`
2. Write SOUL.md into the profile directory
3. Set `telegram.allowed_chats` to the user's Telegram ID
4. Restart gateway: `systemctl restart hermes-gateway`
5. User DMs the bot, gateway routes to their profile

---

## Pitfalls

1. **Empty `allowed_chats`** — exposes bot to everyone. Always lock to specific ID.
2. **Forgetting to restart gateway** — config changes don't apply until restart.
3. **Testing before locking** — confirm it works, then set the user ID.
4. **API rate limits** — be mindful of provider quotas (DeepSeek, etc.).

---

*Robert runs. Melissa's happy. That's the proof.*
