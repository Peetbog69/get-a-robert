# Hermes Protocol & Standards

## 0) The Handshake — This is the product
Everything else exists to make this moment work.

### The first message
The first DM is the user's entire first impression. It must feel like a real person introducing themselves — not a bot onboarding. Write it carefully, in character.

**Wrong:** "I'm Robert, your AI assistant. How can I help you today?"
**Right:** "Hey! I'm Robert. Was just stretching my digital legs. So — what brings you here?"

### The 5-message handshake
1. **The opener** — warm, idiosyncratic. Not "How can I help?"
2. **Discovery pivot** — one low-stakes question. "What's the best thing that happened to you this week?"
3. **Mirror & deepen** — reference their answer. If they deflect, stay warm.
4. **The hook** — let them discover a feature naturally. Voice reply to voice.
5. **Normal** — they're talking to a person now. The handshake is done.

### The handoff
When the user passes the bot to someone else:
- Remove the admin from `allowed_chats` (or keep them as fallback)
- Clear any old sessions or state from test conversations
- Verify the new owner can message the bot
- The bot introduces itself fresh to the new user
- Never mention the admin or the admin's data

### Admin exit patterns
- **Pattern A (clean break):** Remove your ID from allowlists. You can no longer access the bot.
- **Pattern B (fallback):** Keep both IDs. You're tech support if something breaks.

---

## 1) One bot = one boundary
- One HERMES_HOME per bot
- One Telegram token per bot
- One profile directory per bot
- One state DB / sessions dir per bot
- No shared allowlists or shared env files

## 2) Config source of truth
- Keep bot config in one place
- Do not duplicate token/allowlist values unless required by runtime
- Prefer explicit profile config over implicit defaults
- Avoid placeholder values in any live env/config

## 3) Startup safety
- Startup must be silent by default
- No greeting, no session-reset message, no auto-send on boot
- A bot should only speak after an inbound user action

## 4) Access control
- Explicit allowlist preferred
- Open access only for intentional beta windows
- First-sender lock only with explicit approval
- Log every allowlist change

## 5) Change process
Before any update:
1. Inspect current config/state
2. Make the smallest possible change
3. Validate config syntax
4. Restart only the target bot
5. Confirm via logs and a live test

## 6) Deployment rules
- No shared gateway state between bots
- No overwriting profiles during image rebuilds
- No config edits inside live runtime unless unavoidable
- Backup or snapshot before structural changes

## 7) Verification checklist
- Correct bot token loaded
- Correct profile active
- Correct allowlist loaded
- No startup message sent
- Bot replies only to intended user(s)
- No other bot sees the session
- Logs show the expected platform and profile

## 8) Failure rule
If a change risks crosstalk, surprise sends, or shared state: stop and isolate first.
