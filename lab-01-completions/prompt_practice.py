"""Copilot completion practice in Python.

Instructions:
1. Read the comment, signature, or docstring.
2. Put your cursor where the implementation should go.
3. Let Copilot suggest the code.
4. Review the result before accepting.
"""

from __future__ import annotations

from typing import Any, Optional


# ------------------------------------------------------------
# Section 1: Comment-driven completion
# ------------------------------------------------------------

# Exercise: Function that validates an email address.
# Challenge: Let Copilot generate a simple validation approach,
# then evaluate whether it is too strict, too loose, or just right.
def validate_email(email: str) -> bool:
    pass


# Exercise: Function that parses a CSV row into a dict with given fieldnames.
# Example:
# parse_csv_row("Ada,Lovelace,London", ["first_name", "last_name", "city"])
# should return {"first_name": "Ada", "last_name": "Lovelace", "city": "London"}
def parse_csv_row(row: str, fieldnames: list[str]) -> dict[str, str]:
    pass


# Exercise: Recursive function to flatten a nested list.
# Example:
# flatten_nested_list([1, [2, [3, 4]], 5]) -> [1, 2, 3, 4, 5]
def flatten_nested_list(values: list[Any]) -> list[Any]:
    pass


# ------------------------------------------------------------
# Section 2: Type-hint-driven completion
# ------------------------------------------------------------

def get_top_scores(scores: list[int], limit: int = 3) -> list[int]:
    """Return the highest scores in descending order.

    If limit is less than 1, return an empty list.
    """
    pass



def word_frequencies(text: str) -> dict[str, int]:
    """Count how often each lowercase word appears in the text.

    Ignore leading/trailing punctuation and skip empty tokens.
    """
    pass


# ------------------------------------------------------------
# Section 3: Docstring-first approach
# ------------------------------------------------------------

def find_user_by_id(users: list[dict[str, Any]], user_id: int) -> Optional[dict[str, Any]]:
    """Return the first user dict whose id matches user_id.

    Args:
        users: A list of dictionaries like {"id": 1, "name": "Ada"}
        user_id: The integer id to search for

    Returns:
        The matching user dictionary if found, otherwise None.
    """
    pass



def summarize_expenses(expenses: list[dict[str, Any]]) -> dict[str, float]:
    """Calculate simple expense summary metrics.

    Each expense item contains:
    - category: str
    - amount: int | float

    Return a dictionary with:
    - total: sum of all amounts
    - average: average amount, or 0.0 for an empty list
    - max: largest amount, or 0.0 for an empty list
    """
    pass
