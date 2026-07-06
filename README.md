# SLAPP DM Agent

An AI agent that handles customer DM enquiries for [SLAPP](https://instagram.com/slappverse), my cookie brand — built on Groq running Llama 3.3 70B, with multi-turn conversation memory and a system prompt engineered to reply exactly like I would.

## Demo

A real conversation with the agent:

````
Customer: i want cookies
SLAPP bot: heyy, what kinda cookies are you in the mood for? we've got classic, brownie,
comfort, and velvety - or you can mix and match, totally up to you. single cookie or a box?

Customer: what is comfort
SLAPP bot: our comfort cookie is a cinnamon cookie, it's a pretty classic flavor. we think
it's a great choice if you're lookin' for somethin' a little warmer and cozier.

Customer: i loveee chocolate alott
SLAPP bot: then you'll prob love our classic SLAPP or brownie SLAPP. classic has choco chips
and brownie is more fudgy and brownie-like. we can do a box with a mix of both, or just one,
lemme know what you're thinkin'

Customer: hmm waht do you reccoment
SLAPP bot: if you're lookin' to try both classic and brownie, i'd say go for the 5-cookie box.
you can get like 3 of one and 2 of the other, or any mix you want.

Customer: ok
SLAPP bot: so that's a 5-cookie box with a mix of classic and brownie SLAPP. that'll be
₹99 * 4 = ₹396, you get the 5th one free. i'll let you know about delivery pricing when
i know your location, cool?
````

Note what's happening: correct combo math (Buy 4 Get 1 Free), an upsell from "i want cookies" to a 5-box, brand-accurate tone, and it never invents delivery fees it doesn't know.

## How it works

**Model & API** — Llama 3.3 70B via Groq's API (chosen for speed — replies feel instant, which matters for DMs).

**Multi-turn memory** — the full conversation history is maintained as a message list and sent with every API call, so the agent tracks context across the whole chat ("ok" in the demo resolves correctly to the 5-box recommendation from two turns earlier). No trimming yet — fine for DM-length conversations, a token-window strategy is on the roadmap.

**Prompt engineering** — the system prompt encodes the business (flavours, pricing, combos, Porter delivery, 8 PM order cutoff) plus strict tone rules. The interesting parts:

- A *banned phrases list* ("absolutely!", "happy to help", "certainly!") — the fastest way to stop a model sounding like a support bot is telling it exactly which words support bots use
- Explicit uncertainty handling: anything not in its knowledge (exact delivery fees, custom orders) gets "I'll check and get back to you" instead of a hallucinated answer
- Few-shot examples of real question→reply pairs to lock the voice

## Setup

````bash
pip install groq python-dotenv
````

Create a `.env` file in the project root:

````
GROQ_API_KEY=your_key_here
````

Run:

````bash
python3 agent.py
````

## What's next

- **Instagram integration** — currently a CLI tool; the goal is drafting replies directly against real DMs
- **Business system connection** — SLAPP runs on a [Flask/PostgreSQL management system](https://github.com/samairaaleesa-lgtm/slapp-business-system) I built; connecting the agent to live stock and order data would let it check availability and place orders, not just talk
- **Memory management** — token-aware history trimming for longer conversations
- **Tool use** — delivery quote lookups, order status checks
````
````

