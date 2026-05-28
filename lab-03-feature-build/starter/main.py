"""Starter file for the Task Manager CLI lab.

Use Copilot completions for the straightforward parts.
Use Copilot Chat when you want help with JSON persistence, validation,
or refactoring the command loop.
"""

from __future__ import annotations

import json
from pathlib import Path

DATA_FILE = Path(__file__).with_name("tasks.json")


def load_tasks() -> list[dict]:
    """Load tasks from the JSON data file.

    Return an empty list if the file does not exist, is empty,
    or contains invalid JSON.
    """
    pass



def save_tasks(tasks: list[dict]) -> None:
    """Save the provided task list to the JSON data file."""
    pass



def get_next_task_id(tasks: list[dict]) -> int:
    """Return the next integer task id based on the existing task list."""
    pass



def add_task(tasks: list[dict], title: str) -> dict:
    """Add a new task with a unique id and completed=False.

    Raise ValueError if the title is blank after trimming whitespace.
    """
    pass



def list_tasks(tasks: list[dict]) -> None:
    """Print a readable list of tasks to the console.

    Helpful prompt idea:
    - include the id
    - show whether the task is complete
    - handle the empty list case cleanly
    """
    pass



def complete_task(tasks: list[dict], task_id: int) -> bool:
    """Mark the matching task as completed.

    Return True if a task was updated, otherwise False.
    """
    pass



def delete_task(tasks: list[dict], task_id: int) -> bool:
    """Delete the task with the matching id.

    Return True if a task was deleted, otherwise False.
    """
    pass



def print_menu() -> None:
    """Print the CLI menu options for the user."""
    pass



def main() -> None:
    """Run the Task Manager CLI.

    Suggested workflow:
    1. Load tasks
    2. Show menu
    3. Accept a command
    4. Call the right helper
    5. Save changes when needed
    6. Loop until the user exits
    """
    pass


if __name__ == "__main__":
    main()
