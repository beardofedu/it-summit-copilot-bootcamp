"""Reference solutions for Lab 01 (Python)."""

from __future__ import annotations

import re
import string
from typing import Any, Optional



def validate_email(email: str) -> bool:
    pattern = r"^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$"
    return bool(re.match(pattern, email))



def parse_csv_row(row: str, fieldnames: list[str]) -> dict[str, str]:
    values = [value.strip() for value in row.split(",")]
    padded_values = values + [""] * max(0, len(fieldnames) - len(values))
    return {field: value for field, value in zip(fieldnames, padded_values)}



def flatten_nested_list(values: list[Any]) -> list[Any]:
    flattened: list[Any] = []
    for value in values:
        if isinstance(value, list):
            flattened.extend(flatten_nested_list(value))
        else:
            flattened.append(value)
    return flattened



def get_top_scores(scores: list[int], limit: int = 3) -> list[int]:
    if limit < 1:
        return []
    return sorted(scores, reverse=True)[:limit]



def word_frequencies(text: str) -> dict[str, int]:
    frequencies: dict[str, int] = {}
    for token in text.split():
        word = token.strip(string.punctuation).lower()
        if not word:
            continue
        frequencies[word] = frequencies.get(word, 0) + 1
    return frequencies



def find_user_by_id(users: list[dict[str, Any]], user_id: int) -> Optional[dict[str, Any]]:
    for user in users:
        if user.get("id") == user_id:
            return user
    return None



def summarize_expenses(expenses: list[dict[str, Any]]) -> dict[str, float]:
    if not expenses:
        return {"total": 0.0, "average": 0.0, "max": 0.0}

    amounts = [float(expense.get("amount", 0)) for expense in expenses]
    total = sum(amounts)
    return {
        "total": total,
        "average": total / len(amounts),
        "max": max(amounts),
    }
