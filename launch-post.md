# Launch draft — ModelWatch

## Title

ModelWatch: a public changelog for AI API model changes

## Body

AI providers change model IDs, retire models and move aliases. The information is public, but it is spread across pricing pages, model tables and deprecation notices.

I built the first small version of ModelWatch to test one question:

> Would developers use a source-linked feed of model deprecations, retirements and important provider changes?

The first version is intentionally small:

- OpenAI, Anthropic and Google Gemini;
- public provider sources only;
- before/after information where available;
- replacement model and effective date;
- no payment and no account required during the beta test.

Examples currently tracked:

- Google Gemini 2.5 Flash Image — shutdown listed for October 2, 2026.
- OpenAI gpt-5.4-cyber — removal listed for October 1, 2026.
- Anthropic Claude Opus 4.1 — lifecycle table records retirement and a replacement.

I am looking for developers who would use this in a real project. What would matter most to you?

1. model shutdown alerts;
2. price change alerts;
3. capability or parameter changes;
4. a JSON/API feed;
5. webhooks for GitHub, Slack or CI.

The project is a research beta. I am collecting feedback before adding billing or building a full API.

## Do not publish until

- the repository exists;
- all event dates are checked again;
- the launch URL is added;
- the issue intake has been tested.
