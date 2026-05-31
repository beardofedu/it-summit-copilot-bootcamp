"""JSON file persistence for the Contact Book application.

Handles reading and writing the contacts list to a local JSON file.
Designed to be resilient to missing or malformed data files.
"""

from __future__ import annotations

import json
from pathlib import Path

DEFAULT_DATA_FILE = Path(__file__).with_name("contacts.json")


def load_contacts(filepath: Path = DEFAULT_DATA_FILE) -> list[dict]:
    """Load contacts from the JSON data file.

    Returns an empty list if the file does not exist, is empty,
    or contains invalid JSON.

    Args:
        filepath: Path to the JSON file. Defaults to contacts.json
                  in the same directory as this module.

    Returns:
        A list of contact dictionaries.
    """
    if not filepath.exists():
        return []

    try:
        raw_text = filepath.read_text(encoding="utf-8").strip()
        if not raw_text:
            return []
        data = json.loads(raw_text)
        if isinstance(data, list):
            return data
        return []
    except (json.JSONDecodeError, OSError):
        return []


def save_contacts(contacts: list[dict], filepath: Path = DEFAULT_DATA_FILE) -> None:
    """Save the contacts list to the JSON data file.

    Args:
        contacts: The list of contact dictionaries to persist.
        filepath: Path to the JSON file. Defaults to contacts.json
                  in the same directory as this module.
    """
    filepath.write_text(json.dumps(contacts, indent=2), encoding="utf-8")
