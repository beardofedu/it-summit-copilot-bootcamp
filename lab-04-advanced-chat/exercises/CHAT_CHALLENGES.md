# Chat Challenges

Work through these in order. Each one increases the level of reasoning and context management required.

## Beginner challenge

### Use `/explain` to understand a function

Pick a function from `solutions/lab-03/task_manager.py` and ask:

```text
/explain What does this function do? What edge cases does it handle?
```

Goal:
- confirm you can use Chat to understand unfamiliar code quickly

## Intermediate challenge

### Use `/test` to generate tests for lab-03 code

Prompt example:

```text
/test Generate a complete pytest test suite for the task manager in #file:solutions/lab-03/task_manager.py
```

Goal:
- see how Chat proposes test coverage
- review whether the generated tests match real acceptance criteria

## Advanced challenge

### Use Chat with `#file` references to refactor across two files

Suggested files:
- `lab-03-feature-build/starter/main.py`
- `solutions/lab-03/task_manager.py`

Prompt example:

```text
Using #file:lab-03-feature-build/starter/main.py and #file:solutions/lab-03/task_manager.py, suggest a refactor that separates persistence logic from CLI interaction.
```

Goal:
- practice scoping the conversation with file references
- compare a starter design with a completed design

## Expert challenge

### Chain multiple Chat turns to build a feature incrementally with full tests

Suggested flow:

1. Ask Chat to add a priority field to tasks
2. Ask Chat to update list output to show priorities
3. Ask Chat to update persistence logic if needed
4. Ask Chat to generate tests for the new behavior
5. Ask Chat to document the change

Prompt examples:

```text
Add a priority field to the task manager and keep the app beginner-friendly.
```

```text
Now update the list output so priorities are visible when listing tasks.
```

```text
Now generate tests for add, list, and persistence behavior with priorities.
```

Goal:
- learn to treat Chat like an iterative collaborator instead of a one-shot generator

## Reflection questions

After each challenge, ask yourself:
- Was my prompt scoped clearly enough?
- Did Chat use the right files and assumptions?
- What follow-up prompt improved the result the most?
- What still required my own judgment?
