# ModelWatch — validation experiment

## Objective

Test whether developers with a real multi-provider AI application will request a source-linked change feed and a way to receive actionable alerts. Measure concrete behaviour, not reach.

## Baseline

At the 2026-09-14 audit:

- the public page and GitHub Pages deployment worked;
- the repository had 0 stars, 0 forks, 0 open issues and 0 pull requests;
- no external beta requests or customer conversations were recorded.

This is a clean baseline, not evidence that the idea has failed.

## Hypothesis and target user

**Hypothesis:** a developer maintaining production or near-production software that uses two or more AI providers will request a source-linked diff when it can reveal migration work before an outage, cost increase or capability mismatch.

**Initial ICP:** indie SaaS builders, AI-agent developers, LLM gateways and small engineering teams. Exclude people who only want a generic model list; current catalogue data is already widely available.

## Experiment design

### Step 1 — Prepare

- Keep the public changelog small and source-linked.
- Collect provider, model/API, requested change, project context, desired delivery and beta commitment.
- Use public GitHub issues as the transparent signal channel.
- Do not collect passwords, API keys or private email addresses.
- Do not create billing or payment infrastructure during this test.

### Step 2 — Distribute

Post the launch to one relevant developer community at a time, only after approving the exact channel and copy. Record the URL, timestamp and approximate audience. Do not use cold outreach or spam.

### Step 3 — Observe

For every issue or public reply, record:

- source and date;
- provider and model/API;
- requested event type;
- project context and whether it is production-related;
- requested delivery: issue, email/RSS, webhook, API or MCP;
- stated beta commitment;
- strength and next action.

### Step 4 — Learn

After the first three qualified signals, update only the most repeated request. Do not add providers or integrations because of a single speculative suggestion.

## Signal hierarchy

**Strong**

- a developer describes a real application or migration risk;
- a developer requests the same delivery feature as someone else;
- a developer agrees to test a private beta;
- a developer offers an explicit paid commitment after scope and price are shown.

**Medium**

- a developer submits a specific provider/model request;
- a developer asks how to consume the feed or webhook.

**Weak**

- page views, likes or stars without context;
- generic compliments;
- a free download without a request;
- traffic from an irrelevant audience.

## Decision gate after seven days

**Continue to a monitored feed prototype** if there are 10 qualified requests, 3 real use cases, 2 repeated paid-feature requests or 1 committed beta tester.

**Narrow the wedge** if there is specific pain but the audience or delivery format is unclear.

**Stop or pivot** if the only signal is passive traffic or if developers consistently prefer existing catalogues without needing historical diffs or alerts.

## Validation log

Use one line per signal. Keep the log factual and do not publish private contact details.

| date | source | provider/model | requested change | project context | desired delivery | action | strength | next step |
|---|---|---|---|---|---|---|---|---|

## Public links

- Demo: <https://igorvelho.github.io/modelwatch/>
- Repository and issues: <https://github.com/igorvelho/modelwatch/issues>
