# Lab 03 — Feature Build: Task Manager CLI

This is the centerpiece lab for the session.

## What we're building

A simple **Task Manager CLI** in Python that lets a user:
- add tasks
- list tasks
- mark tasks complete
- delete tasks
- save tasks to a JSON file

## Why this lab matters

This lab combines everything from earlier sections:
- good prompts
- inline completions for boilerplate
- Chat for multi-step logic and debugging
- reviewing generated code as you go

## Recommended workflow

### Use completions for:
- function bodies from clear signatures + docstrings
- small helper functions
- repetitive boilerplate
- simple list/dict processing

### Use Chat for:
- persistence design
- error handling strategy
- command parsing improvements
- refactoring after the first working version
- generating tests or docs if you have extra time

## Step-by-step path

1. Open `starter/main.py`
2. Read the docstrings and comments first
3. Start by generating the task loading and saving helpers
4. Implement `add_task` and `list_tasks`
5. Implement `complete_task` and `delete_task`
6. Finish the `main()` command loop
7. Run the program and test each command manually
8. Refine messages and validation with Chat

## Checkpoints

### Checkpoint 1
You can start the CLI and it does not crash immediately.

### Checkpoint 2
You can add a task and see it in the list output.

### Checkpoint 3
Tasks persist after restarting the app.

### Checkpoint 4
You can mark a task complete and delete a task by id.

### Checkpoint 5
Invalid input is handled cleanly with helpful messages.

## Stretch goals for fast finishers

- Add due dates
- Add task priorities
- Add filtering by complete/incomplete
- Add a `clear-completed` command
- Ask Chat to generate tests for your persistence logic
- Ask Chat to improve the CLI help text

## Suggested prompts

### Completion-friendly prompt style

- Clear function names
- Type hints
- Descriptive docstrings
- Small chunks of work at a time

### Chat prompt examples

- “Using this file, help me implement safe JSON persistence.”
- “Refactor my command loop to be easier to read.”
- “What edge cases am I missing in this task manager?”
- “Generate tests for add, complete, and delete behavior.”

## Success criteria

A good lab outcome is not perfect architecture. A good outcome is:
- the app works
- you used Copilot intentionally
- you can explain when you used completions vs. Chat

If you get stuck, compare your code with `../solutions/lab-03/task_manager.py` after giving it an honest attempt.
