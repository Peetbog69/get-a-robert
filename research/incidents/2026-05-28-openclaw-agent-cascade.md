# OpenClaw Agent Self-Sabotage — Breakdown & Fix

> **Date:** 2026-05-28
> **Machine:** Whitey67 (CachyOS, fish shell)
> **Root cause:** OpenClaw agent with unrestricted tool access writing invalid config values

---

## What Broke (Three Cascading Failures)

### 1. Fish shell lost `openclaw` command

**Symptom:** `fish: Unknown command: openclaw`

**Cause:** `.npm-global/bin` was only added to PATH by `~/.bashrc` — which fish never reads. The terminal launches fish directly, bypassing bash entirely. When the agent didn't directly cause this, the fish/bass PATH gap had always existed — it just wasn't noticed until something else broke and the cache cleared.

**Fix:** Added `fish_add_path /home/gravy/.npm-global/bin` to `~/.config/fish/config.fish`

```fish
# npm global packages
fish_add_path /home/gravy/.npm-global/bin
```

---

### 2. OpenClaw gateway refused to start

**Symptom:** Gateway dead, `openclaw gateway start` aborted with config validation error

**Cause:** The agent wrote an invalid value into `models.providers.google.api`. The allowed values are a short list (`openai-completions`, `google-generative-ai`, `anthropic-messages`, etc.) and the agent wrote something outside that list. Config validator rejected the entire file.

**Fix:** `openclaw doctor --fix` auto-restored from last-known-good backup

```bash
openclaw doctor --fix
openclaw gateway start
```

---

### 3. SSH account locked by pam_faillock

**Symptom:** SSH password rejected despite being correct

**Cause:** Multiple failed SSH attempts (probably from mobile, fat-fingering) triggered `pam_faillock` — a security module that temporarily locks accounts after consecutive auth failures. The password was correct, the account was just locked.

**Fix:** Reset the fail counter

```bash
sudo faillock --user gravy --reset
```

---

## Prevention: Lock the Config

The core problem: the OpenClaw agent has the same filesystem permissions as the user. It can write to its own config file. When it hallucinates config values, the validator catches them — but only after the damage is done and the gateway is down.

**Solution:** `chattr +i` — the Linux immutable flag. Makes a file read-only even to its owner. The agent can still read the config, but any write attempt fails.

```bash
sudo chattr +i ~/.openclaw/openclaw.json
```

To verify:

```bash
lsattr ~/.openclaw/openclaw.json
# Should show: ----i-----------------
```

**When you need to legitimately change the config:**

```bash
sudo chattr -i ~/.openclaw/openclaw.json   # unlock
openclaw config set <key> <value>           # make changes
sudo chattr +i ~/.openclaw/openclaw.json   # re-lock
```

**Factory backup saved at:** `~/.openclaw/openclaw.json.factory` — if config gets corrupted somehow, restore from this.

---

## Recovery Quick Reference

If the agent somehow breaks things again (e.g., if you temporarily unlock the config):

| Problem | Fix |
|---------|-----|
| `openclaw` not found in fish | `exec bash && exec fish` or check `fish_add_path` |
| Gateway won't start (config error) | `openclaw doctor --fix` then `openclaw gateway start` |
| SSH password rejected | `sudo faillock --user gravy --reset` |
| Config completely hosed | `cp ~/.openclaw/openclaw.json.factory ~/.openclaw/openclaw.json` |

---

## Deeper Fix: Restrict Agent Tool Access

The immutable flag is a band-aid — the real fix is preventing the agent from writing configs in the first place. Options:

1. **OpenClaw tool profile** — Set `tools.profile` to something restricted that doesn't include file write tools
2. **Container/workspace isolation** — Run the agent in a container or chroot where `~/.openclaw/` is outside its reach
3. **Separate agent user** — Run the agent as a different user that only has read access to configs

These require more setup but provide structural protection rather than just locking individual files.

---

## Appendix A: Exact Fix Commands

```bash
# 1. Fish PATH fix — add npm-global bin to fish config
fish_add_path /home/gravy/.npm-global/bin
# Added to ~/.config/fish/config.fish

# 2. OpenClaw gateway fix — restore from last-good backup
openclaw doctor --fix

# 3. SSH lockout fix — reset pam_faillock counter
sudo faillock --user gravy --reset

# 4. Lock OpenClaw config against future agent writes
sudo chattr +i /home/gravy/.openclaw/openclaw.json

# 5. Hermes group access fix — open allowed_chats
sed -i "s/allowed_chats: ''/allowed_chats: '*'/" /home/gravy/.hermes/config.yaml

# 6. Telegram BotFather group access fix
# /mybots → select bot → Bot Settings → Group Privacy → Turn off
# THEN remove and re-add bot to group
```

## Appendix B: Lessons Learned

1. **Agents with write access to their own configs will eventually corrupt them.** The fix: `chattr +i` on all agent config files, or restrict tool profiles.
2. **Fish doesn't read .bashrc.** PATH entries from bash configs are invisible to fish. Always use `fish_add_path` in config.fish.
3. **pam_faillock silently locks accounts.** Too many failed SSH attempts → account locked even with correct password. Check `journalctl -u sshd` first.
4. **`openclaw doctor --fix` is the safety net.** It auto-restores from last-known-good when config validation fails. Keep `.last-good` backups.
5. **BotFather Group Privacy blocks group adds.** Not a config issue — it's a Telegram permission. `/mybots → Bot Settings → Group Privacy → Turn off`, then re-add the bot.
