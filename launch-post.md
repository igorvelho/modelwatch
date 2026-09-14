# Launch post — ModelWatch

## Title

Show HN: ModelWatch — a source-linked changelog for AI API changes

## Body

AI providers change model IDs, retire models, move aliases and update pricing. The information is public, but it is spread across pricing pages, model tables and deprecation notices.

I built the first small version of ModelWatch to test one question:

> Would developers maintaining real applications use a source-linked feed of model changes to find migration work before production breaks?

Demo: https://igorvelho.github.io/modelwatch/

The first version is intentionally small:

- OpenAI, Anthropic and Google Gemini;
- public provider sources only;
- before/after information where available;
- replacement model and effective date;
- no account, payment or customer integration.

Examples currently tracked:

- Google Gemini 2.5 Flash Image — shutdown listed for October 2, 2026.
- OpenAI GPT-5.4-Cyber — removal listed for October 1, 2026.
- Anthropic Claude Opus 4.1 — lifecycle table records retirement and a replacement.

The repository and source data are public:

https://github.com/igorvelho/modelwatch

I am looking for developers who use two or more AI providers in a real project. What would matter most to you?

1. model shutdown alerts;
2. price change alerts;
3. capability or parameter changes;
4. a JSON/API feed;
5. webhooks for GitHub, Slack or CI.

If this is relevant, use **Request beta access** on the demo and submit the generated GitHub issue with a real use case. Please do not include secrets or private contact details.

This is a research beta. I am collecting concrete use cases before adding billing or building a full API. Feedback about the scope and the event format is welcome.
