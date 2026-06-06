# 🦞 Clawmon's Command Center — Ampersand

**Last updated:** 2026-06-06

---

## 🏛️ Product Pillars (From Tyler)

1. **It's a person, not a product.** Mom calls him Robert. She doesn't "use" him. Language shapes everything.
2. **Less is more.** Don't announce features. Just *do* them. The discovery is the experience.
3. **Respect the consumer's intellect.** People aren't stupid. They've been burned by AI hype. Let them figure it out.
4. **The image matters.** Not just a logo — the feeling of the thing. Warm, clean, like a person texting you.
5. **Word of mouth is the channel.** It's how Robert spread. The product sells itself through "talk to this person."

---

## 🔥 Active

| Priority | Task | Status | Owner |
|----------|------|--------|-------|
| P0 | **Pricing model finalize** | 🟡 In discussion — BYOK $7/mo flat, Hosted $25/mo, possible Lite $15/mo | Tyler + Clawmon |
| P0 | **Onboarding script** — 5-message sequence | 📝 Script drafted, needs review | Tyler |
| P1 | **Website / beta intake page** | ⏳ Basic HTML landing page, possibly Gumroad for payments | Tyler + Clawmon |
| P2 | **Beta user pipeline** | 🟡 Only Melissa active. Need 3-5 more. | Tyler |
| P2 | **Email integration (Himalaya)** | 🟡 Installed, waiting on Gmail creds | Tyler |

---

## 🎉 June 3 — What We Did

| Task | Notes |
|------|-------|
| **OpenAI switch ✓** | gpt-5.4-mini daily driver (was DeepSeek V4 Flash) |
| **ElevenLabs voice ✓** | Key added, Clara/Elli voice, modeled eleven_multilingual_v2 |
| **Whisper API ✓** | Can transcribe voice messages now (gpt-4o-transcribe) |
| **Exa key ✓** | Saved to ~/.credentials/ for Robert's search |
| **Model registry fix ✓** | Added `max_completion_tokens` compat for GPT-5.x |
| **Old session logs ✓** | Cleaned up, only curated daily notes remain |
| **MEMORY.md ✓** | Updated with current state |

## 📋 Backlog

| Priority | Task | Notes |
|----------|------|-------|
| P1 | **Pricing finalization** | BYOK $7/mo, Hosted $25/mo, Lite $15/mo? |
| P1 | **Website landing page** | HTML intake form, Ampersand branding |
| P1 | **Gumroad setup** | For payment processing |
| P2 | **Beta pipeline** | 3-5 users, feedback loop |
| P2 | **Email integration** | Gmail app password for Himalaya |
| P3 | **Multi-agent group chat** | Tyler + mom + Robert + Clawmon |
| P3 | **iOS node pairing** | Camera/location/screen when paired |
| P3 | **ElevenLabs voice clone** | Custom Clawmon voice |
| P4 | **Local ops model (Whitey)** | Run Llama/Qwen for health checks, log parsing, housekeeping |
| P4 | **Local TTS (XTTS v2)** | GPU-based TTS at ElevenLabs quality, voice cloning capable |

---

## 🗺️ Ampersand — Roadmap

### Phase 0: Foundation ✅ (mostly)
- [x] Product pillars defined
- [x] Research complete (parasocial psych, onboarding, competitor analysis)
- [x] Onboarding deep dive — 6K words
- [x] Robert deployed & hardened
- [x] Product name: Ampersand
- [ ] Name finalized across all branding
- [ ] Onboarding script reviewed & finalized
- [ ] Visual identity / website
- [ ] Pricing locked

### Phase 1: Beta (current)
- [ ] Beta user pipeline (3-5 people)
- [ ] Email integration
- [ ] Voice notes working
- [ ] Feedback loop established

### Phase 2: Polish
- [ ] Iterate on personality based on feedback
- [ ] Trial timer / payment processing
- [ ] Pricing pages live
- [ ] Public landing page

### Phase 3: Scale
- [ ] Automated bot provisioning
- [ ] Referral system (word of mouth amplifier)
- [ ] Mom as case study
- [ ] Public launch

---

## 💰 Pricing (Current Thinking)

| Tier | Price | Who |
|------|-------|-----|
| **BYOK** | $7/mo flat | Tech users who bring own API keys |
| **Lite** | $15/mo | Hosted but cheaper model (DeepSeek/nano) |
| **Hosted** | $25/mo | Full experience, no setup needed |

*Still in discussion — first real customer will validate pricing.*

---

## Infrastructure

| Machine | Purpose | Status |
|---------|---------|--------|
| **Whitey67** (local) | Astra, OpenClaw | ✅ Running |
| **VPS** (216.128.154.45) | Robert | ✅ Running, 1GB RAM, ~400Mi free |

### VPS Services
- `hermes-gateway.service` — Robert (Melissa) ✅ running
