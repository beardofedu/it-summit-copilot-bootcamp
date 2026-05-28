"""Reference solution for the Task Manager CLI lab."""

from __future__ import annotations

import json
from pathlib import Path

DATA_FILE = Path(__file__).with_name("tasks.json")



def load_tasks() -> list[dict]:
    if not DATA_FILE.exists():
        return []

    try:
        raw_text = DATA_FILE.read_text(encoding="utf-8").strip()
        if not raw_text:
            return []
        data = json.loads(raw_text)
        if isinstance(data, list):
            return data
        return []
    except (json.JSONDecodeError, OSError):
        return []



def save_tasks(tasks: list[dict]) -> None:
    DATA_FILE.write_text(json.dumps(tasks, indent=2), encoding="utf-8")



def get_next_task_id(tasks: list[dict]) -> int:
    if not tasks:
        return 1
    return max(task.get("id", 0) for task in tasks) + 1



def add_task(tasks: list[dict], title: str) -> dict:
    cleaned_title = title.strip()
    if not cleaned_title:
        raise ValueError("Task title cannot be blank.")

    task = {
        "id": get_next_task_id(tasks),
        "title": cleaned_title,
        "completed": False,
    }
    tasks.append(task)
    return task



def list_tasks(tasks: list[dict]) -> None:
    if not tasks:
        print("No tasks found.")
        return

    print("\nTasks:")
    for task in tasks:
        status = "✓" if task.get("completed") else " "
        print(f"[{status}] {task.get('id')}: {task.get('title')}")



def complete_task(tasks: list[dict], task_id: int) -> bool:
    for task in tasks:
        if task.get("id") == task_id:
            task["completed"] = True
            return True
    return False



def delete_task(tasks: list[dict], task_id: int) -> bool:
    for index, task in enumerate(tasks):
        if task.get("id") == task_id:
            del tasks[index]
            return True
    return False



def print_menu() -> None:
    print("\nTask Manager")
    print("1. Add task")
    print("2. List tasks")
    print("3. Mark task complete")
    print("4. Delete task")
    print("5. Exit")



def prompt_for_task_id() -> int:
    raw_value = input("Enter task id: ").strip()
    if not raw_value.isdigit():
        raise ValueError("Task id must be a number.")
    return int(raw_value)



def main() -> None:
    tasks = load_tasks()

    while True:
        print_menu()
        choice = input("Choose an option: ").strip()

        if choice == "1":
            title = input("Task title: ")
            try:
                task = add_task(tasks, title)
                save_tasks(tasks)
                print(f"Added task #{task['id']}: {task['title']}")
            except ValueError as error:
                print(error)
        elif choice == "2":
            list_tasks(tasks)
        elif choice == "3":
            try:
                task_id = prompt_for_task_id()
            except ValueError as error:
                print(error)
                continue

            if complete_task(tasks, task_id):
                save_tasks(tasks)
                print(f"Marked task #{task_id} complete.")
            else:
                print(f"Task #{task_id} was not found.")
        elif choice == "4":
            try:
                task_id = prompt_for_task_id()
            except ValueError as error:
                print(error)
                continue

            if delete_task(tasks, task_id):
                save_tasks(tasks)
                print(f"Deleted task #{task_id}.")
            else:
                print(f"Task #{task_id} was not found.")
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid option. Please choose 1, 2, 3, 4, or 5.")


if __name__ == "__main__":
    main()
