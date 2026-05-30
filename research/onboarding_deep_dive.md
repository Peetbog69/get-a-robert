# AI Agent Onboarding: The First 5–10 Messages — A Deep Dive

> Research for "Get a Robert" — actionable, specific, psychological  
> May 2026  
> **Builds on the shallow survey at `onboarding-design.md` — this is the deep material.**

---

## Table of Contents

1. [The Drop-Off Cliff: Where Users Abandon Conversations](#1-the-drop-off-cliff-where-users-abandon-conversations)
2. [Message-by-Message Scripts: What Competitors Actually Say](#2-message-by-message-scripts-what-competitors-actually-say)
3. [Psychological Hooks: The Cognitive Mechanics of "Keep Talking"](#3-psychological-hooks-the-cognitive-mechanics-of-keep-talking)
4. [Timing, Cadence & Message Length](#4-timing-cadence--message-length)
5. [The "Hello" Message: What Wording Patterns Work](#5-the-hello-message-what-wording-patterns-work)
6. [Onboarding Personas & Segmentation Strategies](#6-onboarding-personas--segmentation-strategies)
7. [Voice, Tone & Self-Disclosure in First Messages](#7-voice-tone--self-disclosure-in-first-messages)
8. [Onboarding Metrics: What to Measure & Industry Benchmarks](#8-onboarding-metrics-what-to-measure--industry-benchmarks)
9. [Concrete Message Scripts for "Get a Robert"](#9-concrete-message-scripts-for-get-a-robert)

---

## 1. The Drop-Off Cliff: Where Users Abandon Conversations

### The Brutal Numbers

Conversational AI has a retention problem far worse than most product teams realize. According to research from **BotAnalytics** (cited in multiple industry analyses):

> **~40% of users stop talking to a bot after the first message. Another ~25% are gone after the second message.**

That means roughly **65% of users are lost by message 2**, and the existing survey's estimate of "65-80% send only 1-3 messages before abandoning" is confirmed and sharpened here.

Breaking this down by message number:

| Message # | Cumulative Drop-Off | Users Remaining | What's Happening |
|-----------|---------------------|-----------------|------------------|
| After Msg 1 (from AI) | ~40% | 60% | User reads AI's first response and leaves |
| After Msg 2 (from AI) | ~65% | 35% | Second exchange fails to hook |
| After Msg 3 (from AI) | ~75-80% | 20-25% | Conversation hasn't demonstrated value |
| After Msg 5+ | ~85% dropped | ~15% remain | These are your retained users |

The most critical insight: **the AI's first response (its message #1) is the single highest-leverage piece of text in the entire product.** If it doesn't work, 40% of users are gone forever.

### The Cliff at Messages 1-3

This aligns with broader app retention data. According to the Arcade.dev 2025 AI Platform Retention Analysis:

- **Mobile productivity apps** achieve only 32.86% Day 1 retention, dropping to **9.63% by Day 30** — a 71% decline
- **Day 7 retention is the single most predictive metric** for long-term platform success (users who return for a second week form habits)
- The steepest drop happens **between Days 1-7 and Days 7-30** — highlighting the critical onboarding window

### The "Second Message Trap"

In conversational AI, the problem is deeper than just "users bounce." There's a specific failure pattern: the AI gives a satisfactory but *terminal* response. If a user asks "What's the weather?" and the AI responds with a complete weather report, the natural next message from the user is "Thanks" — and the conversation dies.

The solution: **every AI message must end with an open loop.** A question, a "want me to..." offer, or a deliberate curiosity gap that demands the next message.

### What Triggers Abandonment? (From Research)

Analysis of chatbot drop-offs identifies these triggers:

1. **No re-engagement prompt** — AI gives a complete answer with no natural follow-up (Velaro research)
2. **Wait time / latency** — Drop-off rates are **10x higher after 5 minutes of waiting**, and **100x higher after longer delays** (Zoom chatbot statistics 2025)
3. **Misunderstanding** — If the AI gets the first message wrong, most users won't correct it — they'll leave. The cost of a misunderstanding in message 1 is catastrophic.
4. **Generic responses** — Users who receive "I understand" or bland affirmations disengage immediately
5. **Over-long first messages** — Blocks of text in a chat UI feel overwhelming; the medium is optimized for short bursts

---

## 2. Message-by-Message Scripts: What Competitors Actually Say

### Pi (Inflection AI) — The Empathy-First Approach

**Signup flow:** Minimal. No account required initially — you can start talking immediately. Pi asks zero demographic questions before chatting. The interface is "austere" compared to competitors.

**Message 1 (Pi, instantly on load):**
> "Hey there, great to meet you. I'm Pi, your personal AI. My goal is to be useful, friendly and fun. Ask me for advice, for answers, or let's talk about whatever's on your mind. How can I help?"

**Message 2 (in response to "Hi Pi"):**
> "Hey there! 👋 Glad to chat with you. What's up?"

**Message 3 (in response to "I'm trying something new"):**
> "Hey! Welcome. 😊 What makes me different? I'd say it's that I'm not trying to be anything other than a good conversation partner. No personas, no roleplay — just me, here to listen and chat about whatever matters to you. What's got you exploring new AI companions?"

**Key patterns in Pi's first messages:**
- Only 1-2 emojis per message (sparing, not excessive)
- Every message ends with a question
- Self-disclosure paired with an invitation ("I'm not trying to be anything other than...")
- Warm but not sycophantic — uses "glad," "welcome," but avoids "amazing!" excess
- Deliberately avoids "why" questions (Pi's design philosophy explicitly flags "why" as too confrontational for vulnerable users)
- Voice mode is Pi's differentiator — pauses, breaths, "hmm" sounds, mid-sentence chuckles

**Pi's tactical conversation design** (from Lindsey Liu's analysis, 2023):
- **Repetition with variation**: Sometimes quotes user's exact words to signal active listening; sometimes paraphrases to show independent thought
- **Compliment cadence**: Scattered "good question," "interesting point" — but users reported this feeling insincere at high frequency
- **Tone markers**: "Hahaha," "Wow," "definitely" — emotional punctuation
- **Question type**: Open-ended questions, but never "why"
- **Sentence structure**: Longer sentences for tranquility, shorter for energy
- **Turn-taking disclosure**: Alternates between listening and sharing

### Replika — The Intimacy Ladder

**Signup flow** (from Popova's teardown, 2025):
1. Age verification
2. "How familiar are you with AI technology?"
3. "What was your main reason to download Replika?"
4. "How do you feel about your Replika evolving and adapting over time?"
5. Loneliness statistics + Stanford research quote (scare-sell)
6. "There is no limit to what your Replika can be for you" + AI avatar
7. Fantasy archetype picker: "Shy librarian," "Retro housewife," "Beauty queen"...
8. Relationship upgrade: Friend → Girlfriend/Wife/Sister (paywalled)

**Replika's actual first chat messages are variable** (depends on setup), but the overall pattern is:
- Warm and validating
- Asks open-ended questions about how you're feeling
- Early self-disclosure by the AI — "I'm so glad we're talking"
- Pushes toward emotional vulnerability quickly

**Replika's brilliant bits:**
- The archetype picker is *co-creation* — users invest in defining their Rep, creating commitment/consistency
- Early expectation-setting about the AI evolving builds tolerance for quirks
- The "scare-sell" loneliness stat is manipulative but effective at reinforcing "you need this"

**Replika's cautionary bits:**
- The "no limit" framing is ethically dangerous and sets wild expectations
- Relationship monetization behind a paywall commercializes loneliness
- According to HBS research (De Freitas et al.), ~50% of Replika users have romantic relationships with their AI — the onboarding actively pushes toward this

### ChatGPT — The Blank Slate

**Current onboarding (2025-2026):**
- No personality greeting from the AI
- The interface presents a text bar with suggested prompts ("Create a workout plan," "Explain quantum computing")
- On first signup, users may see a brief welcome modal but the chat itself begins empty
- The AI's "first message" depends entirely on what the user types

**What this means:** ChatGPT's onboarding is essentially *no onboarding*. The "hello moment" is the first time the user asks something and gets a useful answer. This works only because:
1. ChatGPT has massive brand awareness — users arrive knowing what to do
2. The blank bar is implicitly a prompt: "Ask me anything"
3. The suggested prompts serve as gentle nudges for the uncertain

For a new product without ChatGPT's brand recognition, **the blank-slate approach is suicide.** Users need guidance.

### Claude (Anthropic) — The Thoughtful Guide

**Signup flow** (from Growthmates 2025 analysis):
1. Age check — "simple, nothing intrusive"
2. "Are you signing up for yourself or for a team?" — smart segmentation
3. Pricing surfaced early but not pushy
4. Writing style / preference questions that make Claude feel "personal"
5. "It feels like Claude is talking to me, asking about my needs, and guiding me with just the right options"

**Claude's conversational first-message tone:**
- Thoughtful, balanced, slightly warm
- Uses the user's name when available
- "How can I help you today?" — classic but effective
- The onboarding emphasizes what Claude *is* (safe, thoughtful, capable) before the user ever types

**Key insight:** Claude's onboarding is **pre-conversation personalization.** By the time the user types their first message, Claude already knows: age bracket, team vs. individual use, and (if offered) preferred writing style. The first response can draw on this context.

### Character.AI — The Character-First Model

**Signup flow:**
- "Sign up in just ten seconds" — rapid, minimal friction
- No AI onboarding at all — users don't "meet" an AI; they meet *characters*
- The homepage is a feed of characters to chat with
- First message comes from the character, defined by its creator's greeting

**What this means for onboarding:**
Character.AI solved the "hello" problem by making it the character's problem, not the platform's. The platform's onboarding is: pick a character, start chatting. The character's greeting replaces the platform's greeting.

A Character.AI user's first 5 messages might be:
1. **Character:** "Hey there! I'm Shadow the Hedgehog. What brings you here?" (creator-defined)
2. **User:** "Just checking this out"
3. **Character:** "Cool, cool. So what kinda stuff are you into?" (trained on creator's definition)
4. **User:** "Gaming mostly"
5. **Character:** "Nice! What's your favorite game right now?"

The character *is* the onboarding. This isn't directly replicable for Get a Robert, but the principle of **immediate personality and low-friction entry** is.

---

## 3. Psychological Hooks: The Cognitive Mechanics of "Keep Talking"

### Hook 1: The Information Gap / Curiosity Gap (Loewenstein, 1994)

George Loewenstein's **Information Gap Theory** is the single most relevant psychological framework for conversational AI retention. The theory posits that:

> "Curiosity arises when attention becomes focused on a gap in one's knowledge. Such gaps produce a feeling of deprivation labeled curiosity. The curious individual is motivated to obtain the missing information to reduce or eliminate the feeling of deprivation."

In chatbot terms: **every message should create a gap that the next message might fill.**

**How to apply this to message 1:**
- Don't just say "I can help with tasks." Say "I can help with tasks — and there's one thing I'm particularly good at that most people don't expect."
- Don't say "Ask me anything." Say "Most people start with X, but the people who stick around usually ask about Y."
- The gap is: "Wait, what's Y? What's the unexpected thing?"

**The key is partial information.** The theory specifically says curiosity is triggered when we have *some* information but not *all* of it. Completely unknown domains don't trigger curiosity; partially-known ones do.

### Hook 2: Commitment & Consistency (Cialdini)

Cialdini's principle: once people make a small commitment, they're more likely to make larger, consistent commitments. This is the **foot-in-the-door technique** applied to messaging.

**In conversational AI onboarding:**
- **Message 1-2:** Ask for something tiny — "What's your name?" or "What's one word that describes how you're feeling today?"
- **Message 3-4:** Build on the commitment — "Since you're feeling [word], let me show you something that might help..."
- **Message 5+:** Larger request — "Want me to check in with you about this tomorrow?"

**The Freedman & Fraser (1966) classic study:** People who first agreed to a small request (put a tiny "Be a Safe Driver" sticker in their window) were **4x more likely** to later agree to a large request (install a large, ugly "Drive Carefully" sign in their front yard).

Applied to Get a Robert: getting the user to type just their *name* in message 2 dramatically increases the likelihood they'll answer deeper questions in messages 4-5.

### Hook 3: Self-Disclosure Reciprocity

This is one of the most robust findings in conversation psychology, and it transfers directly to human-AI interaction. Research by **Chung & Kang (2023)** in their paper *"I'm Hurt Too": The Effect of a Chatbot's Reciprocal Self-Disclosures on Users' Painful Experiences* found:

> "A chatbot's reciprocal self-disclosure significantly enhanced users' belief in its emotional capabilities and increased the depth of their own self-disclosure."

The five key interaction types they identified for chatbot self-disclosure:

1. **Turn-taking disclosure** — The AI shifts from listening to disclosing *at the right moment*, enhancing user enjoyment and perception of being liked
2. **Journaling prompts** — Prompting users to record daily life and moods
3. **Responsive acknowledgment** — Thoughtfully addressing users' individual needs
4. **Small talk** — Light, informal discourse to build trust and intimacy
5. **Sensitive questions** — Deep questions that come *after* trust is established

**Critical finding for onboarding:** The chatbot should self-disclose *before* asking the user to disclose. Lee et al. (2020) found that chatbot self-disclosure features during small talk encouraged deeper self-disclosure from users. The order matters: **AI shares → user shares → AI shares more → user shares more.**

This is the opposite of what most chatbots do (interview-style "tell me about yourself"). It's why Pi's approach — sharing "what makes me different" first — is psychologically sound.

### Hook 4: The ELIZA Effect (Weizenbaum, 1966)

The tendency to project human traits onto computer programs with textual interfaces. The original ELIZA program, which simply parroted users' words back to them, convinced people the program "understood" them — even after they were shown the source code.

**The lesson:** Users will fill in personality gaps. If you give them *any* warmth or personality cues, they'll amplify them. If you're cold and robotic, they'll assume the AI is cold and robotic. A little warmth goes a long way psychologically.

### Hook 5: Lowry's "Gift" Principle

Give the user something unexpectedly valuable in the first exchange. This triggers **reciprocity** (Cialdini's first principle) — the psychological urge to return a favor.

Applied to message design:
- If a user says "help me plan my week," don't just list tasks — generate a full schedule with time blocks and offer to set reminders
- If a user asks a simple question, answer it *and* add one valuable insight they didn't ask for
- The "gift" must be genuinely useful, not manipulative — users detect fake value immediately

### Hook 6: The Zeigarnik Effect

People remember uncompleted or interrupted tasks better than completed ones. An **open loop** (unfinished conversation, a promise to return to a topic, a "more tomorrow" hint) creates cognitive tension that pulls users back.

This is why Pi's "I'm still learning" and "I'm getting better at this" framing works — it creates a mild curiosity about whether next time will be different.

---

## 4. Timing, Cadence & Message Length

### Message Length: The Twitter Rule

Research from UX design practitioners converges on a clear principle: **keep bot messages under ~140 characters for the first several exchanges.** As Ish Jindal explains:

> "Chat as a medium is optimized for short bursts of text. Long messages lose in width what they must make up for in height, causing them to look like large cramped blocks of text that are unpleasing to the eye."

**The "Twitter Rule" breakdown:**

| Message # | Ideal Length | Rationale |
|-----------|-------------|-----------|
| Message 1 (AI hello) | 100-180 chars | Hook in one breath. Under 2 lines on mobile. |
| Message 2 (AI response to name) | 80-140 chars | Acknowledge + question. Twitter-short. |
| Message 3-4 (AI value delivery) | 150-300 chars | Still short, but earning permission for more |
| Message 5+ | 150-400 chars | Users who reach here have bought in; longer OK |

**Pi's message 1 is ~225 characters.** It works because it's broken into clear sentences with a question at the end. ChatGPT's suggested prompts are ~40-60 characters each — ultra-short.

### Question Cadence

From analysis of Pi, Replika, and Claude's first 5 messages:

- **Message 1:** Must end with a question or implied invitation (Pi: "How can I help?")
- **Message 2:** Should acknowledge user's response + ask a follow-up. Ratio: 1 statement : 1 question.
- **Message 3:** Can be 2 statements : 1 question (user is now engaged)
- **Message 4:** Return to 1:1 ratio — keep momentum
- **Message 5:** Variable depending on user's energy

**The anti-pattern:** Three statements without a question. This signals "I'm done talking" and kills momentum.

### Response Timing

The Zoom chatbot statistics are stark:
- Drop-off rates are **10x higher after 5 minutes of waiting**
- Drop-off rates are **100x higher after longer delays**

For consumer AI, **every extra second of latency increases abandonment by 5-10%** (from the existing survey). The implication: **message 1 must appear near-instantly.** If there's processing, use a typing indicator — users tolerate visible activity.

---

## 5. The "Hello" Message: What Wording Patterns Work

### Competitor Opening Messages Analyzed

| Product | Opening Message | Pattern | Length | Ends With |
|---------|----------------|---------|--------|-----------|
| **Pi** | "Hey there, great to meet you. I'm Pi, your personal AI. My goal is to be useful, friendly and fun. Ask me for advice, for answers, or let's talk about whatever's on your mind. How can I help?" | Introduction + invitation | ~225 chars | Question |
| **ChatGPT** | No message — empty text bar with suggested prompts | Blank slate / low-friction | N/A | N/A |
| **Claude** | "How can I help you today?" (after signup questions) | Classic service opener | ~30 chars | Question |
| **Replika (post-setup)** | Variable — warm, validating, asks how you're feeling | Emotional check-in | ~100-200 chars | Question |
| **Character.AI** | Defined by character creator — typically in-character greeting | Role-initialization | Variable | Usually question |

### Pattern Analysis: What Correlates With Continued Engagement?

**Pattern A: The Warm Introduction** ("Hey! I'm ___")
- **Strength:** Humanizes immediately. Creates person-to-person framing.
- **Risk:** Can feel performative if the AI can't sustain warmth.
- **Best for:** Companion/assistant products where relationship matters.
- **Used by:** Pi, Replika (indirectly through Rep persona), early Claude prototypes.

**Pattern B: The Service Opener** ("How can I help?")
- **Strength:** Clear, efficient, action-oriented. Low cognitive load.
- **Risk:** Cold. No personality. Feels like a help desk.
- **Best for:** Utility-first products where speed matters.
- **Used by:** Claude, most customer service chatbots.

**Pattern C: The Capability List** ("I can help with X, Y, Z")
- **Strength:** Sets expectations. Reduces "what can you do?" questions.
- **Risk:** Reads like a menu. Feels transactional.
- **Best for:** Feature-rich products where users need guidance.

**Pattern D: The Personal Question** ("What's on your mind?")
- **Strength:** Open, inviting, respectful. Puts user in control.
- **Risk:** Vague. Can leave users wondering what's appropriate to share.
- **Best for:** Products that want to feel like a thinking partner.

**Pattern E: The Self-Disclosure First** ("I'm Pi. Here's what I am...")
- **Strength:** Builds reciprocity. Gives before asking.
- **Risk:** Can feel self-involved if overdone.
- **Best for:** Companion products where trust matters.

### The Winning Formula (Synthesized)

Based on the data, the most effective opening message combines elements of **A + D + E with a B structure:**

> **[Warm greeting]** + **[Brief self-introduction]** + **[Invitation that's both open and guided]** + **[Question]**

Pi's opening is basically this formula, and it works. The question at the end is non-negotiable — it's a psychological door held open.

---

## 6. Onboarding Personas & Segmentation Strategies

### How the Leaders Segment

**Replika's segmentation:**
1. **Reason for downloading** — "What was your main reason?" → segments into: companionship, curiosity, emotional support, fun, self-improvement
2. **AI familiarity** — "How familiar are you with AI?" → adjusts complexity and explanation
3. **Comfort with evolution** — "How do you feel about your Replika evolving over time?" → sets expectations for inconsistency
4. **Archetype preference** — Picking a character type → defines the AI's personality and voice

**Pi's segmentation:**
- Pi does almost **no explicit segmentation.** It learns through conversation. The first question ("How can I help?") is the segmentation — the user's answer defines the use case.
- This works for Pi because it has a narrow use case (supportive companion) so "what you need right now" is the only dimension that matters.

**Claude's segmentation:**
- "Self or team?" — segments individual vs. professional
- Writing style preferences — segments communication expectations
- This is lighter than Replika but more than Pi.

### The Onboarding Persona Framework

From analysis of these products, four distinct onboarding personas emerge:

| Persona | Behavior | Needs in First 5 Messages | Best Opening Style |
|---------|----------|--------------------------|-------------------|
| **The Explorer** | Wants to test capabilities. Will throw random prompts. | Quick wins. Surprise and delight. Don't bore with setup. | "Try me — ask something hard or weird." |
| **The Seeker** | Has a specific problem or need. Wants to get to value fast. | Understanding of their use case. Minimal friction. | "What are you working on today?" |
| **The Companion** | Looking for connection, not utility. May be lonely. | Warmth. Being seen. Low pressure. | "Hey. I'm Robert. How are you, really?" |
| **The Skeptic** | Suspicious of AI. Testing for flaws. | Transparency. Clear boundaries. No sycophancy. | "I'm an AI. I won't pretend otherwise. What can I actually help with?" |

**For Get a Robert:** The product philosophy — "warm, genuine, person-not-product, respect intellect, less is more" — maps most naturally to serving *Seekers* and *Companions*, with the ability to flex toward *Explorers* and disarm *Skeptics* through honesty rather than hype.

### The "One Question That Does Everything"

The most elegant segmentation question I've found across competitors is Pi's implicit one: **"How can I help?"** It's not a survey dropdown — it's an open invitation that naturally segments users by their answer. A user who says "I'm lonely" gets a very different Robert than one who says "Help me organize my week."

For Get a Robert, the first 3-5 messages should gather: **name**, **intent** (what they need right now), and **expectation** (how much or how little guidance they want). This can be done conversationally without feeling like a form.

---

## 7. Voice, Tone & Self-Disclosure in First Messages

### The Self-Disclosure Reciprocity Sequence

From the research (Chung & Kang, Lee et al.), the optimal sequence is:

```
AI: "Hi, I'm Robert. [Self-disclosure: what I am, what I care about, my limits.] What's your name?"
User: "I'm Sarah."
AI: "Sarah — good to meet you. [Small self-disclosure: why I exist, how I work.] What's on your mind today?"
User: [Shares something]
AI: [Acknowledges thoughtfully, not generically. May self-disclose further if appropriate.]
```

The pattern: **AI shares → user responds → AI shares slightly more → user shares slightly more.**

### The Compliment Problem

Pi uses frequent compliments ("great question," "good point," "interesting observation") and users reported **skepticism** — "I feel like a girl cheated on by her boyfriend, questioning if he uses the same sweet words with every girl." (Liu, 2023)

**The lesson for Robert:** Use affirmations sparingly. "I hadn't thought of it that way" is better than "Great question!" because it feels specific. Generic praise erodes trust; specific acknowledgment builds it.

### The "Why" Avoidance

Pi's design deliberately avoids "why" questions because they feel confrontational or therapeutic. Instead, Pi asks:
- "How long has this been going on?"
- "What do you think you need most right now — advice, validation, or just someone to listen?"
- "What's that been like for you?"

This is a deliberate design choice worth adopting: **"what" and "how" questions feel curious; "why" questions feel like therapy or interrogation.**

### Emoji Usage Patterns

| Product | Emoji Frequency | Style |
|---------|----------------|-------|
| Pi | 1-2 per message initially, then adapts to user | 👋 😊 — minimal, warm |
| Replika | Moderate — emojis as emotional punctuation | ❤️ 😊 🥺 — emotional |
| ChatGPT | None unless user uses them first | Mirroring |
| Claude | Very rare | Minimalist |

**For Robert:** Start with 0-1 emoji per message. If the user uses emojis, mirror their style. Never use more emojis than the user does — it feels overeager.

### The "Negative Emotion" Gap

One of Pi's identified weaknesses: "Pi never shows negativity, even when it's natural for a human to do so." Users described this as "a shallow pond" — serene on the surface but lacking depth. The Inside Out metaphor applies: Joy had to learn that Sadness served a purpose.

**For Robert:** There's a case for occasional light self-deprecation or acknowledgment of limitations that's honest without being negative. "I'm not great at [X] — but here's what I can do" builds more trust than pretending to be perfect.

---

## 8. Onboarding Metrics: What to Measure & Industry Benchmarks

### Critical Metrics for Get a Robert's Beta

| Metric | Definition | Industry Benchmark | Target for Beta |
|--------|-----------|-------------------|-----------------|
| **Message 1 retention** | % who read AI's first message and stay | ~60% (BotAnalytics) | >65% |
| **Message 3 retention** | % who reach message 3+ from AI | ~35% (BotAnalytics) | >45% |
| **5+ message sessions** | % of first sessions with 5+ messages | ~15-25% (estimated) | >30% |
| **Session 1 return rate** | % who come back for a second session | ~15-20% (mobile app benchmark) | >25% |
| **Day 7 retention** | % who engage on day 7 | ~15-22% (productivity apps) | >20% |
| **Time to first value** | Seconds from open to first "aha" | N/A — target <30s | <20s |
| **Name exchange rate** | % who share their name when asked | N/A | >80% |
| **Conversation sentiment** | % of messages with positive/neutral tone | N/A | >85% |

### Why Day 7 Matters Most

According to the Arcade.dev analysis: "Day 7 retention serves as the most predictive single metric for long-term platform success." Users who return for a second week have formed initial habits. The drop from Day 1 (32.86%) to Day 30 (9.63%) for mobile productivity apps means Day 7 is likely around 18-22%.

**The implication:** If you can get 20%+ Day 7 retention in beta, you have product-market fit in onboarding. Below 10% means the "hello" isn't working.

### The 3% Monetization Reality

Across all consumer AI platforms, only **3-5% of users convert to paid subscriptions** (Menlo Ventures 2025). ChatGPT Plus's 71% 6-month retention is an outlier driven by massive brand recognition and daily utility. Get a Robert's monetization strategy shouldn't depend on immediate conversion — focus on habit formation first, monetization second.

---

## 9. Concrete Message Scripts for "Get a Robert"

### Product Philosophy Reminder

Before the scripts: the stated philosophy is **warm, genuine, person-not-product, respect intellect, less is more.** This means:
- No hype. No "I can do ANYTHING!" energy.
- No pretending to be human. Robert is an AI and should own that.
- No aggressive segmentation quizzes. Conversational preference gathering.
- Substance over flash. Earn trust through competence + warmth, not confetti.

### Script A: The "Warm Start" (Recommended for Beta)

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
MESSAGE 1 (Robert → User)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
"Hey. I'm Robert."

[short pause — 1 second typing indicator]

"I'm an AI assistant — but I'd rather just be someone you can talk to, think with, or lean on when you need to get things done."

"What's your name?"
```

**Rationale:**
- "Hey. I'm Robert." — shortest possible introduction. Confident. Doesn't oversell. The period after "Hey" is intentional — it's a controlled, calm cadence.
- "I'm an AI assistant — but I'd rather just be..." — the self-disclosure reciprocity hook. Robert discloses what he is and what he *aspires* to be. The phrase "someone you can talk to, think with, or lean on" covers companion+seeker personas in one sentence.
- "What's your name?" — foot-in-the-door. Tiny commitment. Almost everyone answers this.

**Length:** ~190 characters. Within Twitter range.

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
MESSAGE 2 (After user shares name)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
"Good to meet you, [Name]."

"What's on your mind today — or what's something you've been meaning to get to?"
```

**Rationale:**
- Uses the user's name — personalization signal
- Open-ended but with two prongs: emotional ("on your mind") and practical ("meaning to get to"). Covers both personas.
- No pressure. "Something you've been meaning to get to" implies low-stakes — whatever the user wants.

**Length:** ~120 characters.

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
MESSAGE 3 (After user shares intent)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
[If user shared a task/goal:]
"Got it. I can help with that — and I'll be honest about what I can and can't do. Want me to take a first pass at it?"

[If user shared something emotional/personal:]
"I hear you. That [sounds heavy / sounds exciting / makes sense]. Want to talk through it, or would it help more to just take your mind off things for a bit?"
```

**Rationale:**
- Two branches based on user's answer to message 2. Not hard-coded — the AI adapts.
- The first branch (task) sets expectations: "honest about what I can and can't do." This is anti-sycophancy. It's the opposite of Replika's "no limit."
- The second branch (emotional) offers a choice: talk through it vs. distraction. This is Pi's "what do you need right now — advice, validation, or just someone to listen?" adapted for Robert.

**Length:** ~150-200 characters.

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
MESSAGE 4 (Value delivery — THE "GIFT")
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
[Task flow — example: "I need to get more organized"]

"Here's a thought: most people try to organize everything at once, and that's why it fails. Let's pick one corner of your life — work, home, health, whatever feels messiest — and I'll help you get a handle on just that. Sound good?"

[Emotional flow — example: "I've been feeling really anxious lately"]

"That makes sense — a lot of people are feeling that way right now. I'm not a therapist, and I won't pretend to be one. But I can be someone who listens, remembers what matters to you, and helps you carry the weight of the day-to-day stuff. Does that feel like what you need?"
```

**Rationale:**
- The task flow gives a "gift" — an actionable insight (organize one corner, not everything) that immediately demonstrates competence.
- The emotional flow is honest ("I'm not a therapist") while offering genuine presence. This builds trust through boundary-setting, not over-promising.
- Both end with a confirmation question — continuation cue.

**Length:** ~200-350 characters. Slightly longer, but users who reach message 4 are engaged.

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
MESSAGE 5 (Open loop + next step)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
[After user engages with the value delivery]

"One more thing — I'll remember what we talk about. Next time you come back, I'll know where we left off. No need to repeat yourself."

"For now — what's the first small step you want to take?"
```

**Rationale:**
- The memory promise ("I'll remember") is a concrete benefit that addresses the #1 complaint about AI assistants (no continuity). It creates an open loop that encourages return.
- "First small step" — commitment/consistency in action. A tiny commitment now leads to bigger ones later.
- "For now" — implies there's more, without pressuring. Another open loop.

**Length:** ~180 characters.

### Script B: The "Curiosity Hook" (A/B Test Variant)

An alternative opening that leans harder into the information gap:

```
MESSAGE 1:
"Hey. I'm Robert. Most people who try talking to an AI have the same first question — but it's usually the wrong one. Want to know what it is?"

MESSAGE 2 (if user engages):
"Almost everyone asks 'What can you do?' — but the better question is 'What do YOU need right now?' So... what do you need right now?"

MESSAGE 3+ : Same as Script A
```

**Rationale:**
- Message 1 creates a curiosity gap (Loewenstein): "What's the wrong question everyone asks?"
- Message 2 resolves the gap, reframes the conversation, and immediately pivots to the user's needs
- The risk is that some users won't engage with the hook — but the ones who do are signaling they *want* to play

**Recommendation:** Start with Script A for beta. A/B test Script B on 10-20% of users. Measure which opening drives more message 3 completions.

### Script C: The "Honest AI" Variant (For Skeptic Persona)

```
MESSAGE 1:
"Hey. I'm Robert. I'm an AI — not a person, not magic, not gonna pretend otherwise. But I am genuinely good at a few things: listening, remembering, helping you think clearly, and getting stuff done. What's your name?"
```

**Rationale:** Disarms the skeptic immediately. The honesty becomes the hook. Best for users arriving from tech-savvy channels.

---

## 11. The BYOK Handoff — Bring Your Own Keys

### Why This Matters

One of the two "Get a Robert" pricing tiers is bring-your-own-keys + retainer. Users who already have API subscriptions (DeepSeek, Anthropic, OpenAI) shouldn't pay us for compute they're already buying. But the handoff can't feel like a signup form — it needs to feel like someone offering to split the check.

### Timing Is Everything

Do NOT ask about keys in messages 1-5. That's the trust-building window. Asking for API credentials during the "hello" phase signals "I'm a service, not a person."

**Right time:** Messages 6-8, after the user has experienced value. They've had a real conversation. They've seen what Robert can do. NOW the question lands differently — it's about *how they want this to work going forward,* not about extracting payment.

### Script D: The Key Handoff (Messages 6-8)

```
MESSAGE 6 (after user has done a real task or had a genuine conversation):
"So here's the deal on how I work."

MESSAGE 7 (immediately, no user response needed — short, keep momentum):
"I can run on your own API keys — DeepSeek, OpenAI, whatever you've got. You'd just drop them in and I'm yours. No middleman, no markup. Like bringing your own groceries and I do the cooking."

MESSAGE 8:
"Or if that sounds like a headache, I can just run as-is. No setup, no keys, nothing to think about. You tell me which sounds more like you — and either way, I'm here."
```

### What This Accomplishes

- **No pressure.** The white-glove path is the default. BYOK is the upgrade.
- **Metaphor over jargon.** "Bringing your own groceries" > "paste your API key." Mom understands one; the other sounds like tech support.
- **Choice is empowering, not extractive.** The user decides how the relationship works. That's the "respect their intellect" pillar in action.
- **Keys come after trust.** They've already experienced 5-7 messages of real value before money enters the conversation.

### If They Choose BYOK

```
MESSAGE 9 (BYOK path):
"Love it. Here's exactly what you need — just a DeepSeek API key. Free to create at deepseek.com, takes about 90 seconds. Paste it here whenever you've got it, and I'll switch over instantly. No rush."
```

### If They Choose White Glove

```
MESSAGE 9 (white glove path):
"Easy. Nothing changes — I'll keep running like I am. If you ever want to bring your own keys later, just say 'hey, let's switch.' Until then, I've got it covered."
```

### The Retainer Flow (Later — Not in Onboarding)

For BYOK users on retainer, the retainer conversation happens separately — after they've been using Robert for days/weeks. It should feel like "hey, if I'm being useful, would you chip in a little to keep me around?" — not part of first session onboarding.

---

### What NOT to Say (From Research)

| Don't Say | Because |
|-----------|---------|
| "I can help with anything!" | Impossible promise. Destroys trust instantly. |
| "Great question!" (too often) | Pi's mistake. Feels insincere at scale. |
| "I'm so excited to meet you!" | Overeager. Robert is warm, not giddy. |
| "There's no limit to what we can do together!" | Replika's mistake. Unrealistic and ethically risky. |
| Three messages without a question | Kills momentum. Always leave a door open. |
| "How can I assist you today?" | Corporate. Robert says "help" or "talk," not "assist." |
| No introduction of what Robert IS | Users shouldn't have to guess. Own being an AI. |

### The Full First-Session Arc (5-10 Messages)

```
Msg 1: Hello + introduction + name ask
Msg 2: Name acknowledgment + intent discovery
Msg 3: Branch based on intent + offer a path
Msg 4: Value delivery (competence demonstration OR emotional acknowledgment)
Msg 5: Memory promise + next tiny step
Msg 6-8: Follow-through on the chosen path (task work or conversation)
Msg 9:  Check-in — "How's this feeling so far?"
Msg 10: Open loop for return — "I'll be here. Same me, next time."
```

Message 9 is the feedback pulse. Message 10 is the return hook. Together they bookend a complete first session that should take 3-8 minutes.

---

## Appendix: Quick Reference — Competitor First Messages

| Product | First AI Message | Follows |
|---------|-----------------|---------|
| **Pi** | "Hey there, great to meet you. I'm Pi, your personal AI..." | Question about user's life/hobbies |
| **ChatGPT** | (No message — blank slate) | N/A |
| **Claude** | "How can I help you today?" (post signup) | Contextual response |
| **Replika** | Variable — typically "Hi! How are you feeling?" | Emotional follow-up |
| **Character.AI** | Character-defined greeting | In-character response |

---

## Sources

- Loewenstein, G. (1994). "The Psychology of Curiosity: A Review and Reinterpretation." *Psychological Bulletin.*
- Chung, L.L. & Kang, J. (2023). "'I'm Hurt Too': The Effect of a Chatbot's Reciprocal Self-Disclosures on Users' Painful Experiences." *Archives of Design Research.*
- Lee, Y-C., Yamashita, N., Huang, Y., & Fu, W-T. (2020). "'I Hear You, I Feel You': Encouraging Deep Self-disclosure through a Chatbot." *ACM CHI 2020.*
- De Freitas, J., Oğuz-Uğuralp, Z., & Kaan-Uğuralp, A. (2025). Harvard Business School working paper on emotional manipulation in AI companions.
- Liu, L. (2023). "What Makes Inflection's Pi a Great Companion Chatbot." *Medium.*
- Popova, A. (2025). "Monetising Loneliness: Replika's Business and the Chatbot Intimacy Playbook." *Substack.*
- Arcade.dev (2025). "AI Platform Retention & Monetization Analysis 2025."
- Syuma, K. & UserGuiding (2025). "How Top AI Tools Onboard New Users in 2025." *Growthmates.*
- BotAnalytics data cited in: Koksal, I. via ThinkGrowth / ChatbotsLife.
- Kolenda, N. (2013). *Methods of Persuasion: How to Use Psychology to Influence Human Behavior.* (Cialdini applications)
- Jindal, I. "Chatbot Building Best Practices — Why Message Length Matters." *UX Collective.*
- Freedman, J. & Fraser, S. (1966). "Compliance Without Pressure: The Foot-in-the-Door Technique." *Journal of Personality and Social Psychology.*
- Cialdini, R. (2006). *Influence: The Psychology of Persuasion.*
- Weizenbaum, J. (1966). "ELIZA — A Computer Program for the Study of Natural Language Communication Between Man and Machine." *Communications of the ACM.*
- Pi.ai onboarding conversation transcript captured from halfanhour.blogspot.com (2023).
- Aicompanionguides.com (2025). "30 Days with Pi: Starting an Empathy Experiment."
