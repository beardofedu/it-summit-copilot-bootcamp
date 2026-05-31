"""Core contact management logic for the Contact Book application.

Provides CRUD operations for managing a list of contacts.
Each contact is a dictionary with keys: id, name, email, phone.
"""

from __future__ import annotations


def get_next_id(contacts: list[dict]) -> int:
    """Return the next available integer ID for a new contact.

    If the list is empty, starts at 1. Otherwise, returns one more
    than the current maximum ID.
    """
    if not contacts:
        return 1
    return max(contact.get("id", 0) for contact in contacts) + 1


def add_contact(contacts: list[dict], name: str, email: str, phone: str) -> dict:
    """Create a new contact and append it to the contacts list.

    Args:
        contacts: The existing list of contacts (modified in place).
        name: Validated contact name.
        email: Validated contact email.
        phone: Validated contact phone number.

    Returns:
        The newly created contact dictionary.
    """
    contact = {
        "id": get_next_id(contacts),
        "name": name,
        "email": email,
        "phone": phone,
    }
    contacts.append(contact)
    return contact


def search_contacts(contacts: list[dict], query: str) -> list[dict]:
    """Search contacts by name (case-insensitive partial match).

    Args:
        contacts: The list of contacts to search.
        query: The search string to match against contact names.

    Returns:
        A list of contacts whose name contains the query string.
    """
    query_lower = query.strip().lower()
    if not query_lower:
        return []
    return [c for c in contacts if query_lower in c.get("name", "").lower()]


def delete_contact(contacts: list[dict], contact_id: int) -> bool:
    """Delete a contact by its ID.

    Args:
        contacts: The list of contacts (modified in place).
        contact_id: The integer ID of the contact to remove.

    Returns:
        True if a contact was deleted, False if no matching ID was found.
    """
    for index, contact in enumerate(contacts):
        if contact.get("id") == contact_id:
            del contacts[index]
            return True
    return False


def find_contact_by_id(contacts: list[dict], contact_id: int) -> dict | None:
    """Find a single contact by its ID.

    Args:
        contacts: The list of contacts to search.
        contact_id: The integer ID to look for.

    Returns:
        The matching contact dictionary, or None if not found.
    """
    for contact in contacts:
        if contact.get("id") == contact_id:
            return contact
    return None
