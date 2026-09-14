# Launch post — ModelWatch

## Recommended channel

Ask HN. The public page is an interactive research prototype, not yet a production monitoring service, so this asks about the operational problem instead of presenting a signup page as a finished product.

## Title

Ask HN: How do you track AI API model changes before production breaks?

## Body

AI providers change model IDs, retire models, move aliases and update pricing. The information is public, but it is spread across pricing pages, model tables and deprecation notices.

I am testing whether developers maintaining real applications need a source-linked feed of these changes: what changed, when, the before/after values, the official source and the migration action.

I built a small public prototype to make the idea concrete:

https://igorvelho.github.io/modelwatch/

It currently tracks a few source-linked examples from OpenAI, Anthropic and Google Gemini. It is deliberately not a full SaaS yet: no account, payment or customer integration.

For people using two or more AI providers, which of these would be most useful?

1. model shutdown/deprecation alerts;
2. price change alerts;
3. capability or parameter changes;
4. a JSON/API feed;
5. webhooks for GitHub, Slack or CI;
6. something else.

How do you handle this today? Manual documentation checks, provider emails, an internal script, a gateway, or something else? A real production example is especially useful.

Please do not share secrets or private customer information. I am collecting concrete use cases before adding billing or building a full API.
