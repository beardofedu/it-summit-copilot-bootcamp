"""Input validation helpers for the Contact Book application.

These functions validate user-provided data before it is stored.
They are designed to give clear error messages when input is invalid.
"""

from __future__ import annotations

import re


def validate_name(name: str) -> str:
    """Validate and normalize a contact name.

    Rules:
    - Must not be blank after stripping whitespace.
    - Must contain only letters, spaces, hyphens, and apostrophes.
    - Returns the stripped name on success.

    Raises:
        ValueError: If the name is blank or contains invalid characters.
    """
    cleaned = name.strip()
    if not cleaned:
        raise ValueError("Name cannot be blank.")
    if not re.match(r"^[a-zA-Z\s\-']+$", cleaned):
        raise ValueError(
            "Name can only contain letters, spaces, hyphens, and apostrophes."
        )
    return cleaned


def validate_email(email: str) -> str:
    """Validate an email address format.

    Rules:
    - Must not be blank.
    - Must match a basic email pattern (something@something.something).
    - Returns the lowercase, stripped email on success.

    Raises:
        ValueError: If the email is blank or does not match the expected format.
    """
    cleaned = email.strip().lower()
    if not cleaned:
        raise ValueError("Email cannot be blank.")
    pattern = r"^[a-zA-Z0-9._%+\-]+@[a-zA-Z0-9.\-]+\.[a-zA-Z]{2,}$"
    if not re.match(pattern, cleaned):
        raise ValueError(f"Invalid email format: {cleaned}")
    return cleaned


def validate_phone(phone: str) -> str:
    """Validate and normalize a phone number.

    Rules:
    - Strip spaces, dashes, and parentheses.
    - The remaining characters must be digits only.
    - Must have between 7 and 15 digits (inclusive).
    - Returns the digits-only string.

    Raises:
        ValueError: If the phone number is blank or has an invalid number of digits.
    """
    cleaned = re.sub(r"[\s\-()]+", "", phone.strip())
    if not cleaned:
        raise ValueError("Phone number cannot be blank.")
    if not cleaned.isdigit():
        raise ValueError("Phone number must contain only digits (after removing spaces, dashes, and parentheses).")
    if len(cleaned) < 7 or len(cleaned) > 15:
        raise ValueError(
            f"Phone number must have between 7 and 15 digits, got {len(cleaned)}."
        )
    return cleaned
