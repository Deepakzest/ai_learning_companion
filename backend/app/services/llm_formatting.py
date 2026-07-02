import json
import re
from typing import Any, Callable


def _extract_json_fragment(text: str) -> str:
    fenced_match = re.search(r"```(?:json)?\s*(.*?)```", text, re.IGNORECASE | re.DOTALL)
    if fenced_match:
        return fenced_match.group(1).strip()

    start_candidates = [index for index in [text.find("["), text.find("{")] if index != -1]
    if not start_candidates:
        return text.strip()

    start = min(start_candidates)
    end_array = text.rfind("]")
    end_object = text.rfind("}")
    end = max(end_array, end_object)
    if end > start:
        return text[start : end + 1].strip()
    return text.strip()


def parse_llm_json(text: str, default_factory: Callable[[], Any]) -> Any:
    if not text:
        return default_factory()

    fragment = _extract_json_fragment(text)
    try:
        return json.loads(fragment)
    except json.JSONDecodeError:
        return default_factory()
