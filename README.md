# ModelWatch — validation beta

ModelWatch is a small experiment for developers who need to know when AI providers change model lifecycle, pricing, capabilities or aliases.

## Hypothesis

> Developers maintaining an application that uses two or more AI providers will request a source-linked change feed when it helps them identify migration work before production breaks.

The product is **not** another model catalogue. Existing catalogues already expose current prices and capabilities. The proposed wedge is the delta: what changed, when, the before/after values, the official source and the operational action.

## What exists

- public static landing page;
- five source-linked research events from OpenAI, Anthropic and Google;
- provider filters;
- structured GitHub Issue Form for beta signals;
- pre-filled issue link from the landing page;
- no payment, account system or customer integration;
- no claim of customer validation.

## Current status

Audited on 2026-09-14:

- Demo: <https://igorvelho.github.io/modelwatch/>
- Repository: <https://github.com/igorvelho/modelwatch>
- GitHub Pages workflow: passing;
- public repository: 0 stars, 0 forks, 0 open issues and 0 pull requests;
- external customer signals: 0 recorded.

The technical launch is complete. The commercial validation has **not** started because the page has not yet been distributed to a relevant developer audience.

## Validation experiment

### Target user

Indie SaaS and AI-agent developers who deploy against two or more providers and currently discover model changes through manual documentation checks, provider emails or incidents.

### Seven-day test

1. Send qualified developer traffic to the public page through one approved community at a time.
2. Ask each interested person to submit the public beta issue form with a real provider, model or project context.
3. Tag each issue by requested change: deprecation, pricing, capability/limits, alias/behaviour or other.
4. Record whether the person asks for a feed, webhook, API, email/RSS digest or a private beta test.
5. Do not build integrations or accept payment before the decision gate.

### Pass criteria

Continue to a monitored feed prototype if the test produces at least one of:

- 10 qualified beta requests;
- 3 real project/use-case descriptions;
- 2 people requesting the same paid feature;
- 1 developer agreeing to test a private beta when available.

Passive views, likes and unqualified compliments do not pass the test. If only those appear, narrow or stop the idea.

## Send a useful signal

Open the demo, click **Request beta access**, and submit the public GitHub issue. Do not include secrets, private credentials or personal email addresses. A useful response names the provider/model, the change that matters and the application context.

## Run locally

```bash
python3 -m http.server 4173 --directory site
```

Open <http://127.0.0.1:4173>.

The page is self-contained and does not require npm or external JavaScript packages.

## Verification

```bash
python3 scripts/validate.py
```

## Sources used for the initial events

- Google Gemini API pricing: <https://ai.google.dev/gemini-api/docs/pricing>
- Google Gemini models: <https://ai.google.dev/gemini-api/docs/models>
- OpenAI API deprecations: <https://developers.openai.com/api/docs/deprecations>
- Anthropic model deprecations: <https://docs.anthropic.com/en/docs/about-claude/model-deprecations>
