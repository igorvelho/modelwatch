# ModelWatch — launch kit

ModelWatch is a validation-stage product for developers who need to know when AI providers change model lifecycle, pricing or capabilities.

## Current scope

This repository is a **launch kit**, not a production SaaS:

- static landing page;
- five public, source-linked research events;
- provider filters;
- pre-filled GitHub issue intake for beta interest;
- no payment;
- no account system;
- no customer integrations;
- no claim of customer validation.

## Run locally

```bash
python3 -m http.server 4173 --directory site
```

Open <http://127.0.0.1:4173>.

The page is self-contained and does not require npm or external JavaScript packages.

## Public launch checklist

1. Create `igorvelho/modelwatch` as a public GitHub repository.
2. Push this directory to the repository.
3. Enable GitHub Pages from the `site` directory, or publish the same `site/index.html` on a static host.
4. Replace the working-name copy and repository URL if the name changes.
5. Verify each event against its linked provider page immediately before publishing.
6. Publish the launch post in `launch-post.md`.
7. Watch GitHub issues and record interest in `validation.md`.

## Important limitation

The form opens a pre-filled GitHub issue. It becomes a real signal channel only after the repository is public. It does not silently send email or store private data.

## Sources used for the initial events

- Google Gemini API pricing: https://ai.google.dev/gemini-api/docs/pricing
- Google Gemini models: https://ai.google.dev/gemini-api/docs/models
- OpenAI API deprecations: https://developers.openai.com/api/docs/deprecations
- Anthropic model deprecations: https://docs.anthropic.com/en/docs/about-claude/model-deprecations
