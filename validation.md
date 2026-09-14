# ModelWatch — 7-day validation plan

## Objective

Find out whether developers will take a concrete action around model-change monitoring. Do not measure only views or likes.

## Signal hierarchy

Strong:

- a developer opens a beta issue with a real provider/model;
- a developer asks for a webhook or API format;
- a developer shares a repository or production use case;
- a developer agrees to a follow-up beta test.

Weak:

- page views;
- stars without a comment;
- generic compliments;
- social likes;
- free downloads without a request.

## Seven-day procedure

### Day 1 — Publish

- Publish the repository and static page.
- Post the launch draft to one developer community first.
- Do not add payment.
- Record the exact post URL and timestamp.

### Days 2–3 — Observe

- Read every issue and public reply.
- Tag each signal: deprecation, pricing, capability, API, webhook, other.
- Do not argue with negative feedback.

### Days 4–5 — Narrow

- Update the page with the most requested event type.
- Add no new provider unless users ask for it.
- Publish one concrete example from feedback, with permission.

### Days 6–7 — Decide

Continue only if at least one of these is true:

- 10 qualified developers request access;
- 3 developers describe a real project that would use the feed;
- 2 developers ask for the same paid feature;
- 1 developer agrees to test a private beta when available.

Stop or pivot if the only signal is passive traffic.

## What to record

| Field | Example |
|---|---|
| date | 2026-09-14 |
| source | GitHub issue / HN / Product Hunt |
| provider | OpenAI |
| requested event | deprecation |
| project context | internal agent / SaaS / hobby |
| action | issue / request / comment |
| strength | strong / medium / weak |
| next step | reply / ignore / investigate |

## No-payment rule

Do not create a Stripe product or ask for card details during this test. The first gate is concrete interest in the problem, not revenue.
