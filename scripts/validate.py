#!/usr/bin/env python3
"""Small offline checks for the ModelWatch validation beta."""
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data" / "events.json"
HTML = ROOT / "site" / "index.html"


def main() -> None:
    events = json.loads(DATA.read_text())
    assert isinstance(events, list) and len(events) >= 3
    required = {"id", "provider", "type", "model", "status", "summary", "source_url"}
    for event in events:
        assert required <= event.keys(), event
        assert event["source_url"].startswith("https://"), event
        assert event["summary"].strip(), event
    page = HTML.read_text()
    for provider in ("OpenAI", "Anthropic", "Google Gemini"):
        assert provider in page, provider
    for marker in (
        "github.com/igorvelho/modelwatch/issues/new",
        "No payment",
        "validation beta",
        "Do not paste secrets",
        "Project context",
    ):
        assert marker.lower() in page.lower(), marker
    issue_form = ROOT / ".github" / "ISSUE_TEMPLATE" / "beta-interest.yml"
    form = issue_form.read_text()
    for marker in ("name: Beta interest", "id: provider", "id: context", "id: commitment"):
        assert marker.lower() in form.lower(), marker
    print(f"validated {len(events)} public events and launch page")


if __name__ == "__main__":
    main()
