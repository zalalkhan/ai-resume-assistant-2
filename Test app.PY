import json
from unittest.mock import MagicMock

import pytest

import app

GOOD = {
    "summary": "Use Canva.",
    "tools": [
        {"name": "Canva", "description": "Design tool", "best_for": "logos",
         "pricing": "Freemium", "pros": ["Easy", "Templates"], "cons": ["Paid extras"],
         "website": "https://www.canva.com"},
        {"name": "Looka", "description": "Logo maker", "website": "javascript:alert(1)"},
        {"description": "no name"},
        "junk",
    ],
}


def test_parse_json_handles_fences_and_noise():
    assert app.parse_json("```json\n" + json.dumps(GOOD) + "\n```")["summary"] == "Use Canva."
    assert app.parse_json("Sure! " + json.dumps(GOOD) + " Hope it helps")["summary"] == "Use Canva."


def test_parse_json_rejects_text_without_json():
    with pytest.raises(ValueError):
        app.parse_json("no json here")


def test_normalize_keeps_valid_tools_only():
    result = app.normalize_result(GOOD, 5)
    assert [t["name"] for t in result["tools"]] == ["Canva", "Looka"]


def test_good_link_is_kept():
    tool = app.normalize_result(GOOD, 5)["tools"][0]
    assert tool["url"] == "https://www.canva.com" and tool["direct_link"]


def test_unsafe_link_falls_back_to_google_search():
    tool = app.normalize_result(GOOD, 5)["tools"][1]
    assert tool["url"].startswith("https://www.google.com/search?q=Looka")
    assert not tool["direct_link"]


def test_missing_pricing_gets_safe_default():
    tool = app.normalize_result(GOOD, 5)["tools"][1]
    assert tool["pricing"] == "Check website for current pricing"


def test_count_limit_is_respected():
    assert len(app.normalize_result(GOOD, 1)["tools"]) == 1


@pytest.mark.parametrize("bad", [{}, {"tools": "x"}, {"tools": []}])
def test_normalize_raises_when_no_tools(bad):
    with pytest.raises(ValueError):
        app.normalize_result(bad, 3)


def test_prompt_contains_user_input_and_filters():
    prompt = app.build_prompt("make logos", "Free only", "Image & design", 4)
    for text in ("make logos", "Free only", "Image & design", "exactly 4"):
        assert text in prompt
    assert prompt.count("{") == prompt.count("}")


def test_find_tools_retries_once_on_bad_json(monkeypatch):
    client = MagicMock()
    client.models.generate_content.side_effect = [MagicMock(text="oops"), MagicMock(text=json.dumps(GOOD))]
    monkeypatch.setattr(app.genai, "Client", lambda api_key: client)
    result = app.find_tools("logo maker", "Any budget", "Any category", 5, "KEY")
    assert result["tools"][0]["name"] == "Canva"
    assert client.models.generate_content.call_count == 2


def test_find_tools_gives_up_after_two_bad_answers(monkeypatch):
    client = MagicMock()
    client.models.generate_content.return_value = MagicMock(text="still bad")
    monkeypatch.setattr(app.genai, "Client", lambda api_key: client)
    with pytest.raises(ValueError):
        app.find_tools("logo maker", "Any budget", "Any category", 5, "KEY")


def test_report_lists_tool_names():
    report = app.build_report("logo", app.normalize_result(GOOD, 5))
    assert "Canva" in report and "https://www.canva.com" in report
