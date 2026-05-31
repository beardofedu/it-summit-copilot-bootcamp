"""CSV export functionality for the Contact Book application.

Provides a way to export contacts to a CSV file for use in
spreadsheets or other tools.
"""

from __future__ import annotations

import csv
from pathlib import Path


def export_to_csv(contacts: list[dict], filepath: Path | str) -> int:
    """Export contacts to a CSV file.

    Creates a CSV file with columns: id, name, email, phone.
    Overwrites the file if it already exists.

    Args:
        contacts: The list of contact dictionaries to export.
        filepath: The path where the CSV file should be written.

    Returns:
        The number of contacts exported.

    Raises:
        ValueError: If the contacts list is empty.
    """
    if not contacts:
        raise ValueError("No contacts to export.")

    filepath = Path(filepath)
    fieldnames = ["id", "name", "email", "phone"]

    with filepath.open("w", newline="", encoding="utf-8") as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames, extrasaction="ignore")
        writer.writeheader()
        for contact in contacts:
            writer.writerow(contact)

    return len(contacts)
