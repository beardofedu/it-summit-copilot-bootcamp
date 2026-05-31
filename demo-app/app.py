"""Contact Book CLI — A sample application for Copilot demos.

This is the main entry point for the Contact Book command-line application.
Run this file directly to start the interactive menu.

Usage:
    python app.py
"""

from __future__ import annotations

from pathlib import Path

from contacts import add_contact, delete_contact, find_contact_by_id, search_contacts
from export import export_to_csv
from storage import load_contacts, save_contacts
from validators import validate_email, validate_name, validate_phone


def print_menu() -> None:
    """Display the main menu options."""
    print("\n===== Contact Book =====")
    print("1. Add a contact")
    print("2. List all contacts")
    print("3. Search contacts")
    print("4. Delete a contact")
    print("5. Export to CSV")
    print("6. Exit")
    print("========================")


def display_contacts(contacts: list[dict]) -> None:
    """Print a formatted list of contacts to the console."""
    if not contacts:
        print("No contacts found.")
        return

    print(f"\n{'ID':<5} {'Name':<25} {'Email':<30} {'Phone':<15}")
    print("-" * 75)
    for contact in contacts:
        print(
            f"{contact.get('id', ''):<5} "
            f"{contact.get('name', ''):<25} "
            f"{contact.get('email', ''):<30} "
            f"{contact.get('phone', ''):<15}"
        )


def handle_add(contacts: list[dict]) -> None:
    """Prompt the user for contact details and add a new contact."""
    try:
        name = validate_name(input("Name: "))
        email = validate_email(input("Email: "))
        phone = validate_phone(input("Phone: "))
    except ValueError as error:
        print(f"Error: {error}")
        return

    contact = add_contact(contacts, name, email, phone)
    save_contacts(contacts)
    print(f"Added contact #{contact['id']}: {contact['name']}")


def handle_search(contacts: list[dict]) -> None:
    """Prompt the user for a search query and display results."""
    query = input("Search by name: ")
    results = search_contacts(contacts, query)
    if results:
        display_contacts(results)
    else:
        print("No matching contacts found.")


def handle_delete(contacts: list[dict]) -> None:
    """Prompt the user for a contact ID and delete it."""
    raw_id = input("Enter contact ID to delete: ").strip()
    if not raw_id.isdigit():
        print("Error: ID must be a number.")
        return

    contact_id = int(raw_id)
    contact = find_contact_by_id(contacts, contact_id)
    if contact is None:
        print(f"No contact found with ID {contact_id}.")
        return

    if delete_contact(contacts, contact_id):
        save_contacts(contacts)
        print(f"Deleted contact #{contact_id}: {contact.get('name')}")


def handle_export(contacts: list[dict]) -> None:
    """Export all contacts to a CSV file."""
    if not contacts:
        print("No contacts to export.")
        return

    output_path = Path(__file__).with_name("contacts_export.csv")
    try:
        count = export_to_csv(contacts, output_path)
        print(f"Exported {count} contact(s) to {output_path.name}")
    except ValueError as error:
        print(f"Error: {error}")


def main() -> None:
    """Run the Contact Book CLI application."""
    contacts = load_contacts()

    while True:
        print_menu()
        choice = input("Choose an option: ").strip()

        if choice == "1":
            handle_add(contacts)
        elif choice == "2":
            display_contacts(contacts)
        elif choice == "3":
            handle_search(contacts)
        elif choice == "4":
            handle_delete(contacts)
        elif choice == "5":
            handle_export(contacts)
        elif choice == "6":
            print("Goodbye!")
            break
        else:
            print("Invalid option. Please choose 1-6.")


if __name__ == "__main__":
    main()
