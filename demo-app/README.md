# Demo Application — Contact Book CLI

This is a self-contained sample application designed for **presenter demos** throughout the bootcamp session. It provides a realistic codebase with enough complexity to demonstrate all Copilot features in one place.

## What it does

A simple command-line Contact Book that lets you:

- Add contacts (name, email, phone)
- List all contacts
- Search contacts by name
- Delete a contact
- Export contacts to CSV

Data is stored in a local `contacts.json` file.

## How to run

```bash
cd demo-app
python app.py
```

## Why this app exists

The presenter guide (`PRESENTER.md`) references this application across multiple demo sections:

| Demo section | How this app is used |
| --- | --- |
| Section 1: Completions | Show inline suggestions while writing new features |
| Section 2: Chat | Ask Chat to explain functions or suggest improvements |
| Section 4: `/explain` | Explain the `search_contacts` or `export_to_csv` function |
| Section 4: `/fix` | Introduce a bug and use `/fix` to resolve it |
| Section 4: `/test` | Generate tests for the persistence layer |
| Section 4: `/doc` | Add docstrings and improve CLI help text |
| Section 5: CLI | Use `gh copilot suggest` to run or extend the app |

## File overview

| File | Purpose |
| --- | --- |
| `app.py` | Main entry point and CLI menu loop |
| `contacts.py` | Core contact management logic (CRUD operations) |
| `storage.py` | JSON file persistence |
| `validators.py` | Input validation helpers |
| `export.py` | CSV export functionality |

## Demo tips

- The code is intentionally straightforward so attendees can follow along.
- Functions have clear docstrings to support `/explain` demos.
- Validation logic is separated so you can demonstrate scoped Chat prompts.
- The export module is a good target for `/test` since it has clear input/output behavior.
