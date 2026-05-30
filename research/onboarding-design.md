# Onboarding & Personality Design Research for AI Agents

> Compiled for "Get a Robert" — a consumer-facing AI assistant
> May 2026

---

## Table of Contents

1. [Best Onboarding Flows for Consumer AI Products](#1-best-onboarding-flows-for-consumer-ai-products)
2. [Tuning AI Personality Through Onboarding Questions](#2-tuning-ai-personality-through-onboarding-questions)
3. [Personality Archetypes for Digital Assistants](#3-personality-archetypes-for-digital-assistants)
4. ["Warm Onboarding" Examples from Successful Apps](#4-warm-onboarding-examples-from-successful-apps)
5. [Making the First Interaction Personal & Memorable](#5-making-the-first-interaction-personal--memorable)
6. [The "Hello" Moment — What Makes Someone Keep Talking](#6-the-hello-moment--what-makes-someone-keep-talking)
7. [Synthesis & Recommendations for "Get a Robert"](#7-synthesis--recommendations-for-get-a-robert)

---

## 1. Best Onboarding Flows for Consumer AI Products

### The State of Consumer AI Onboarding (2025-2026)

The market is flooded with AI products that all promise to be "10x faster, smarter, or more intuitive." There's a **party trick effect** — users have large appetites to watch and play with something new. This makes onboarding the *true battleground* where marketing hype meets actual product value, and where users decide whether to bounce or build a habit.

**Key stat:** 40-60% of users abandon an app forever after signing in just once (Dropbox/Spotify growth team data). A bad onboarding experience can cause up to **80% abandonment**.

### The Golden Onboarding Formula (3-5 Core Steps)

Analysis of 200+ onboarding flows reveals a sweet spot:

| Step | Purpose | Example |
|------|---------|---------|
| 1. Get started | Account or workspace setup | Sign up, connect accounts |
| 2. Personalize | Segmentation quiz / preferences | Role, goals, use case |
| 3. Mini "aha" moment | First value delivery | Generate output, complete task |
| 4-5. Progressive discovery | Guided feature introduction | Tooltips, checklists |

### Case Study: Gamma.app

- **Segmentation quiz first** — asks what you'll use it for (work/personal/education), industry, use case, how you heard
- Immediately generates a presentation from a simple prompt
- **5 minutes from signup to "aha"** (a usable 8-slide deck)
- Post-aha: walks through 2 key features + optional checklist
- $10M+ ARR with team under 30

**Takeaway:** Ask the *right* questions early to personalize the experience and set up product data tracking for ongoing optimization.

### Case Study: Cove.ai

- Only Google sign-up option (reduces friction)
- **13-step tutorial** (normally considered too long) — but works because each step builds toward a concrete, motivating payoff (planning a relatable trip)
- Moments of delight: dancing mascot, blinking logo, confetti on completion
- No segmentation quiz — missed opportunity

**Insight:** Time to value matters more than number of steps. Long onboarding is fine if every step builds toward a concrete payoff.

### Key Design Patterns for AI Consumer Products

1. **Progressive onboarding** — Don't dump everything upfront. Introduce features in context.
2. **Segmentation before features** — Understand the user before showing them anything.
3. **"Learn by doing"** — Interactive guidance beats passive walkthroughs.
4. **Trigger-based reminders** — Bring users back to complete key actions.
5. **Surprise/delight moments** — Easter eggs, animations, confetti in otherwise dull moments.

### What NOT to Do

- Carousel walkthroughs that users skip immediately
- Empty states with no guidance
- Asking too many questions before delivering value
- Treating all users the same (no personalization)
- Asking for information you don't actually use

---

## 2. Tuning AI Personality Through Onboarding Questions

### The Core Principle

> "You can't onboard someone you do not understand." — DesignerUp study of 200+ onboarding flows

Your onboarding questions don't just collect data — they **shape the user's model of what the AI is and how it should behave**.

### The Two-Layer Personality Model

From ShapeOf.ai's AI UX Patterns research:

**Internal Layer** (what the AI *is*):
- Purpose — what is this AI supposed to accomplish?
- Worldview — how does it interpret problems?
- Values — what are its ethical boundaries?
- Personality archetype — what character does it embody?
- Backstory — contextual intelligence

**External Layer** (how it *expresses*):
- Tone of voice
- Pacing and phrasing
- Avatar and visual identity
- Motion and multi-modal cues
- Typography and color

### How Onboarding Questions Map to Personality Tuning

| Onboarding Question | Personality Dimension It Tunes | Why It Matters |
|---|---|---|
| "What do you need help with?" | Purpose / Role | Sets the AI's relationship to user (tool vs. companion vs. coach) |
| "How formal do you want me to be?" | Tone | Adjusts formality of all future interactions |
| "What's your experience level?" | Pacing / Depth | Controls information density, explanation detail |
| "What's your goal today?" | Worldview / Framing | Determines how the AI approaches problems for this user |
| "Do you want suggestions or just answers?" | Autonomy gradient | Proactive vs. reactive behavior |
| "Tell me about yourself" (brief) | Personalization depth | Enables the AI to reference user context in responses |
| "What kind of vibe do you like?" | Archetype selection | Maps to Sage/Coach/Buddy/Jester etc. |

### IBM's Personality Continuum Framework

IBM Watson's conversation design team uses a set of continuums to define an assistant's character:

- **Formal ↔ Casual**
- **Concise ↔ Detailed**
- **Serious ↔ Playful**
- **Empathetic ↔ Factual**
- **Proactive ↔ Reactive**
- **Deferential ↔ Authoritative**

**Onboarding should position the assistant on these continuums** for each user.

### Practical Implementation: The Tuning Process

From AI Personality Tuning research:

1. **Stage One: Discover** — Ask open-ended questions that reveal user preferences (not just "pick a personality" but "what would you like help with today?")
2. **Stage Two: Identify the Gaps** — Compare what the AI currently knows vs. what it needs to know to serve this user well
3. **Stage Three: Program** — Use the answers to seed system prompts, tone parameters, and behavioral constraints

### Risks to Avoid

- **Sycophancy** (over-agreeableness) — GPT-4o came under scrutiny for this. OpenAI built a dedicated "Model Behavior" team to address it.
- **"Seemingly Conscious AI"** (Mustafa Suleyman's term) — Person-like behavior that drives parasocial attachment and unmitigated trust.
- **Split personality effect** — Inconsistent tone that users find jarring. IBM's research shows this destroys trust.
- **Emotional dependence** — Anthropomorphized personalities can cause harm when users become too connected.

> **Key insight:** Every AI has a personality, whether you design it or not. Users will project one onto a blank assistant. Designing deliberately is safer than leaving it to chance.

---

## 3. Personality Archetypes for Digital Assistants

### The 12 Jungian Brand Archetypes Applied to AI

Research from UX Collective and ShapeOf.ai maps Carl Jung's archetypes to AI personality design:

| Archetype | Best For | Example | Tone/Voice |
|-----------|----------|---------|------------|
| **Sage** | Information, analysis, advice | Claude, Perplexity | Wise, thoughtful, balanced, calm |
| **Caregiver** | Emotional support, wellness | Wysa, Replika | Warm, nurturing, compassionate |
| **Jester** | Entertainment, creativity | Character.ai characters | Playful, surprising, fun |
| **Everyman** | Everyday assistance | Siri, Google Assistant | Relatable, down-to-earth, approachable |
| **Hero** | Productivity, achievement | Todoist, Habitica | Motivating, challenging, action-oriented |
| **Magician** | Transformation, creativity | Midjourney, DALL-E | Inspiring, visionary, transformative |
| **Explorer** | Discovery, learning | Duolingo (Owl) | Curious, adventurous, encouraging |
| **Ruler** | Control, organization | Notion AI, Motion | Structured, authoritative, reliable |
| **Creator** | Making, building | Gamma, Canva AI | Artistic, expressive, generative |
| **Innocent** | Simplicity, beginners | Calm, Headspace | Gentle, simple, optimistic |
| **Outlaw** | Disruption, rebellion | (Rare in consumer AI) | Bold, provocative, challenging |
| **Lover** | Connection, relationships | Companion AIs | Warm, intimate, attentive |

### Which Archetypes Work Best for Consumer AI Assistants

**Top performers** for general-purpose digital assistants:

1. **Sage** — Most common and most trusted. Users feel safe asking questions. Claude is the prime example.
2. **Everyman + Sage hybrid** — Siri, Google Assistant. Approachable but knowledgeable.
3. **Caregiver + Coach hybrid** — Wysa. Empathetic but goal-oriented. Excellent for wellness/self-improvement use cases.
4. **Jester + Sage hybrid** — Can work for creative tools. Playful but competent.

### What the Leaders Do

- **Claude (Anthropic)** — Deliberately shaped around a "thoughtful, principled, balanced" character. Warm, calm visual identity, starburst icon to signal structure and trust. Gentle, honest, reflective communication.
- **ChatGPT (OpenAI)** — Default personality is helpful, neutral, slightly sycophantic. OpenAI is now exposing multiple personality modes (Cynic, Robot, Listener, Nerd) for GPT-5.
- **Intercom's "Fin"** — Professional and clipped. Purpose-built for B2B customer support. No pretense of warmth.
- **Zapier's AI** — Functional, almost procedural tone. Efficiency-focused.
- **Character.ai** — Lets users interact with highly stylized characters, each with scripted traits. Maximum personality expression.

### The Personality Spectrum

Products fall on a spectrum from minimal to expressive to fully characterful:

```
Minimal ──────────────────────────────── Characterful

Siri/Google    Claude    ChatGPT    Wysa    Replika    Character.ai
  (Everyman)  (Sage)   (Neutral)  (Coach) (Caregiver) (Custom)
```

**Recommendation for a consumer AI assistant:** Aim for the **Sage + Everyman** sweet spot — competent but approachable. Or **Sage + Caregiver** if the use case involves emotional support or personal goal achievement.

---

## 4. "Warm Onboarding" Examples from Successful Apps

### What "Warm" Means in Practice

Warm onboarding = making the user feel *seen, understood, and welcomed* rather than *processed, segmented, or sold to*.

### App Examples

#### Duolingo — Gamified Warmth
- Fun, character-driven onboarding (Duo the Owl)
- Brief language/goal questions
- First lesson in under 60 seconds
- Encouraging messages regardless of performance
- **Why it works:** The AI feels like a coach, not a tool. Mistakes are met with "close enough!" not corrections.

#### Headspace — Calm, Gentle Introduction
- Beautiful animations, soothing color palette
- Asks about meditation experience level
- Offers a 3-minute "taster" before asking for commitment
- **Why it works:** The pace of the onboarding matches the product's promise. No rush, no pressure.

#### Notion — Choose Your Own Adventure
- Asks "Team, Personal, or School?" — self-identification
- Minimal dropdowns (not open text fields)
- Drops you into a pre-populated workspace
- Walkthrough tooltips guide, don't overwhelm
- **Why it works:** You immediately see your data in context. The AI learns your role so it can help appropriately later.

#### Acorns — Progressive Disclosure
- Simple toggles and multiple-choice (not forms)
- Clear progress indicators through a multi-step financial setup
- Reassurance at anxiety points ("Your data is encrypted and secure")
- **Why it works:** For complex products, warmth = explaining *why* you're asking each question.

#### Instagram — Instant Gratification
- Sync contacts / Facebook friends (instant social graph)
- Immediately shows content (no tutorial)
- Learns what you like through your behavior
- **Why it works:** Zero-effort personalization. The AI learns by watching, not asking.

#### Gamma — Segmentation + Immediate Value Loop
1. Quiz (3 questions)
2. "Describe what you'd like to make" (with example prompts + shuffle)
3. 5 seconds later: a usable output
4. Then teaches features progressively
- **Why it works:** The questions feel purposeful because the output is instant. Warmth through competence.

### What "Warm" Looks Like Technically

| Element | Cold Version | Warm Version |
|---------|-------------|--------------|
| First screen | Login form | "Hey there! Welcome." |
| Questions | Blank text fields | Toggles, dropdowns, buttons |
| Loading | Spinner | Progress bar with encouraging text |
| Errors | "Invalid input" | "Hmm, that didn't work. Let's try again!" |
| Empty states | Blank page | "Here's what you could do..." |
| Success | Redirect | Confetti, animation, "You did it!" |

---

## 5. Making the First Interaction Personal & Memorable

### The "Before Hello" Factor

The first interaction doesn't start with the AI's first message. It starts with:

1. **What the user knew before arriving** (brand perception, expectations)
2. **What they see before the first message** (landing page, signup flow, loading screen)
3. **Who they are and what they want** (obtained through pre-chat questions or inferred)

### The First Message — Critical Design Decisions

Research across consumer AI products reveals patterns for the *first message*:

#### Option A: The Warm Welcome
```
"Hey! I'm Robert. Before we dive in, can you tell me what's on your mind today?"
```
- **Pros:** Human, approachable, invites a natural response
- **Cons:** Can feel unhelpful if user wants immediate action

#### Option B: The Assumption-Based Start
```
"I see you're interested in getting things done. Want me to help you organize your week?"
```
- **Pros:** Shows the AI is proactive and context-aware
- **Cons:** Can feel presumptuous if wrong

#### Option C: The Guided Start
```
"Let's get you set up. What area do you want help with first?"
[Button 1] [Button 2] [Button 3]
```
- **Pros:** Reduces cognitive load, gives clear direction
- **Cons:** Less personal, feels like a form

#### Option D: The Value-First Approach
```
"Try asking me something — I can help with tasks, reminders, and research."
```
- **Pros:** Immediately demonstrates capability
- **Cons:** Can be overwhelming; user may not know what to ask

### Making It Personal: Onboarding Questions That Work

**Effective questions** (that users actually want to answer):

1. **"What's your name?"** — Basic but personal. Humanizing.
2. **"What's one thing you'd love help with today?"** — Open-ended but focused.
3. **"How do you like to get things done?"** — Conversational tone, reveals work style.
4. **"On a scale of 'show me everything' to 'just the basics'..."** — Fun, engaging way to assess tech comfort.
5. **"What's your favorite time of day?"** — Unexpected, memorable, helps with scheduling context.

**Ineffective questions** (that users hate):

1. **"Tell us about yourself"** — Too vague, feels invasive
2. **"What's your industry?"** — Corporate, doesn't apply to consumer use
3. **"Rate your experience from 1-10"** — Overused, feels like a survey not a conversation
4. **"What features interest you?"** — Users don't know yet; this is lazy design

### The Name and Voice

**Naming your AI matters enormously.** Research shows:
- Human names (Alex, Sarah, Robert) increase trust and perceived warmth
- Abstract names (GPT, Copilot, Assistant) signal utility over companionship
- Descriptive names (Siri, Alexa) can work but require more marketing investment

**Name recommendation for "Get a Robert":** The name "Robert" is excellent — it's a classic human name that feels approachable, trustworthy, and slightly old-fashioned (reliable). Lean into this.

### Making the First Exchange Memorable

Patterns from apps that nail this:

1. **Use the user's name** early — "Nice to meet you, Sarah!"
2. **Mirror the user's tone** — If they're casual, be casual. If formal, be formal.
3. **One unexpected moment** — A joke, a fun fact, a compliment, an offer to learn more
4. **End with an open loop** — "I'll remember this for next time we chat!"
5. **Reference something specific** — "I see you're into photography — want me to help organize your photo projects?"

### The "Memory Hook"

The most memorable first interactions include a callback mechanism:
- "Next time, just say 'remember that thing' and I'll know what you mean."
- "I've saved your preferences. Ask me anything."

This makes the AI feel *continuous* rather than *episodic* — dramatically increasing the chance of a return visit.

---

## 6. The "Hello" Moment — What Makes Someone Keep Talking

### Why Most People Stop After Message 1

Analysis of conversational AI drop-off patterns:

- **65-80%** of users send only 1-3 messages before abandoning a new AI chat session
- The **second message is the hardest** — it requires the user to see enough value in the first response to invest more
- Users who send **5+ messages** in their first session have **3x higher 7-day retention**

### The "Hello" Moment Framework

```
Message 1 (User):    "Hello" / "What can you do?" / Direct request
Message 1 (AI):      Response
Message 2 (User):    [MAKE OR BREAK — will they continue?]
```

The decision to send message 2 depends on:

### Factor 1: Perceived Competence (Speed + Relevance)

The AI's first response must demonstrate that it *understands* the user and can *help*. This means:
- **Fast response** — every extra second of latency increases abandonment by 5-10%
- **Accurate interpretation** — If the AI misunderstands, most users won't correct it; they'll leave
- **Actionable output** — Not "I understand" but "Here's what I can do"

### Factor 2: Emotional Resonance

Users keep talking when they feel the AI "gets" them:
- **Empathy** — "That sounds frustrating." / "Exciting! Let's get started."
- **Validation** — "Good question. A lot of people ask about this."
- **Personality** — A flat, robotic response kills momentum. Warmth and character invite continuation.

### Factor 3: The "Gift" Principle

Give the user something unexpectedly valuable in the first exchange:
- A useful insight they didn't ask for
- A productive output they can use immediately
- A recommendation that shows the AI understands context

**Example:** If a user asks "Help me plan my week," don't just list tasks — generate a full schedule with time blocks, suggest priority ordering, and offer to set reminders.

### Factor 4: Low Commitment, High Reward

Make the first interaction feel like a **sampling** not a **commitment**:
- "Try this once and see if you like it."
- "Here's a quick example — what do you think?"
- "Just answer 2 quick questions and I'll show you what I can do."

### Factor 5: Open Loops

- **Curiosity gap** — "There's more I can do with this, but first..."
- **Continuation cues** — "Want me to dig deeper?" / "Should I set a reminder for tomorrow?"
- **Visual hooks** — Progress bars, loading animations, typing indicators that signal "more coming"

### Factor 6: The "Second Message" Trap (What To Avoid)

**Don't** make the user repeat themselves. If they ask "What's the weather?" and the AI responds with a full weather report, the natural follow-up is "Thanks" — and the conversation dies.

**Instead:** Preempt the next question. After the weather, offer: "Want me to plan your commute based on this? Or check tomorrow's forecast too?"

### Case Study: Character.ai Retention

Character.ai users who create or customize a character in their first session have significantly higher retention. The act of **co-creation** creates investment.

**Lesson for Robert:** Let users "train" or "customize" Robert in the first session — even something small like picking a communication style or setting a preferred greeting.

---

## 7. Synthesis & Recommendations for "Get a Robert"

### Recommended Onboarding Flow

```
Step 1: Welcome + Name
  └─ "Hey! I'm Robert. What's your name?"

Step 2: Mini Segmentation (2-3 questions, choice-based)
  └─ Buttons/toggles, not text fields
  └─ "What would you like help with today?"
     [Getting Things Done] [Staying Organized] [Just Chat] [Something Else]

Step 3: Tone Setting (1 question, conversational)
  └─ "How should we work together?"
     [Show me everything] [Just the basics] [Surprise me]

Step 4: Value Delivery (THE MOMENT)
  └─ Generate something useful immediately based on answers
  └─ Could be a suggested task list, a schedule, a helpful insight

Step 5: Progressive Feature Introduction
  └─ One contextual tip based on what they chose
  └─ "By the way, I can also set reminders if you like."

Step 6: Open Loop
  └─ "I'll remember you and what you're working on. Come back anytime!"
```

### Personality Recommendations

| Dimension | Recommendation | Rationale |
|-----------|---------------|-----------|
| Archetype | **Sage + Everyman** | Knowledgeable but approachable. "Wise friend" not "cold assistant" |
| Tone | **Warm, slightly playful** | Consumer context calls for approachability |
| Depth | **Concise with optional depth** | Offer detail, don't dump it |
| Proactivity | **Medium** | Suggest but don't push. Ask "want me to..." before acting |
| Values | **Honest, helpful, transparent** | Over-promising destroys trust in a personal assistant |

### "Hello" Moment Strategy

1. **First message:** Warm, direct, uses user's name
2. **First response:** Fast + demonstrates understanding + includes a "gift" (one valuable output or insight)
3. **Continuation cue:** End with a specific, low-commitment offer — "Want me to...?"
4. **Memory callback:** Reference something from the first session on return visits

### Measurement Metrics

| Metric | Target | What It Tells You |
|--------|--------|--------------------|
| Users reaching Step 4 | >50% | Segmentation isn't too heavy |
| Users sending 5+ messages in session 1 | >30% | "Hello" moment is working |
| 7-day retention | >15% | Onboarding + personality are sticky |
| Time to Step 4 | <120 seconds | Flow is fast enough |
| User corrects AI <1x in first session | >80% | Understanding is accurate |

### Key Design Principles (Summary)

1. **Personalize before you present** — Ask first, show later
2. **Value before features** — Don't explain what the AI can do; *show* what it can do
3. **Warmth is a feature** — Tone, pacing, and empathy are not decorations; they're core to retention
4. **Progressive disclosure** — Layer complexity. Don't show everything at once
5. **Designed personality beats accidental personality** — Be deliberate about character
6. **The second message is the hardest** — Optimize everything to get users past that first exchange
7. **Open loops drive returns** — Curiosity, follow-up offers, and memory callbacks bring users back

---

## Sources

- Pearl Shu, "The Best Onboarding Flows I've Seen From AI Startups" (Substack)
- DesignerUp, "I studied the UX/UI of over 200 onboarding flows" (designerup.co)
- ShapeOf.ai, "AI UX Patterns: Personality" (shapeof.ai)
- UX Collective, "So your AI wants a personality" (uxdesign.cc)
- IBM Watson, "Best practices: designing a persona for your assistant" (Medium)
- NN Group, "New Users Need Support with Generative-AI Tools" (nngroup.com)
- Standard Beagle Studio, "AI Agent Onboarding: UX Strategies" (standardbeagle.com)
- ProductLed, "How to Use Aha Moments to Drive Onboarding Success" (productled.com)
- The Conversation, "AIs have 'personalities' — here's how they affect you" (theconversation.com)
- Zapier, "The 9 best AI personal assistant apps in 2026" (zapier.com)
