# Feature Spec — Task Manager CLI

## Objective

Build a simple Python Task Manager CLI that demonstrates a realistic workflow using GitHub Copilot for most of the implementation.

## Core features

Your program must support the following actions:

1. **Add task**
   - Accept a task title from the user
   - Create a new task with a unique id
   - Save the task to persistent storage

2. **List tasks**
   - Display all tasks in a readable format
   - Show task id, title, and completion status

3. **Mark complete**
   - Let the user choose a task by id
   - Mark the task as completed
   - Save the updated data

4. **Delete task**
   - Let the user choose a task by id
   - Remove the task
   - Save the updated data

## Technical requirements

- Use **Python**
- Persist data in a **JSON file**
- Validate user input
- Handle common errors gracefully
- Keep the program beginner-friendly and readable

## Data model suggestion

Each task can be stored like this:

```json
{
  "id": 1,
  "title": "Prepare summit slides",
  "completed": false
}
```

## Input validation expectations

At minimum, handle these cases:
- blank task title
- invalid menu choice
- invalid task id
- trying to complete or delete a task that does not exist
- missing or empty JSON data file

## Error handling expectations

- The app should not crash for common user mistakes
- Show helpful messages instead of stack traces for expected issues
- Recover cleanly when the data file is missing or empty

## Copilot usage expectation

**Important:** Use Copilot for at least **80% of the code** in this lab.

That means:
- use inline completions for starter implementations
- use Chat when the logic becomes more complex
- keep your prompts visible in comments/docstrings when useful

The goal is not to hand-code everything. The goal is to practice steering Copilot effectively.

## Acceptance criteria checklist

- [ ] User can add a task
- [ ] User can list tasks
- [ ] User can mark a task complete
- [ ] User can delete a task
- [ ] Data persists between runs in JSON format
- [ ] Blank task titles are rejected
- [ ] Invalid task ids are handled safely
- [ ] Missing data file does not crash the app
- [ ] Code is readable and reasonably organized
- [ ] Copilot was used intentionally for most of the implementation
