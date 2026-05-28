# Example Chat Responses

These are example outputs you might see from Copilot Chat during Lab 04. Exact wording will vary.

## Beginner — `/explain`

**Prompt**

```text
/explain What does complete_task do in #file:solutions/lab-03/task_manager.py?
```

**Example response**

> `complete_task` iterates through the in-memory task list and looks for a task whose `id` matches the provided `task_id`. If it finds a match, it updates the `completed` field to `True` and returns `True`. If no match is found, it returns `False`. One limitation is that it assumes task ids are unique and that each task is represented as a dictionary.

## Intermediate — `/test`

**Prompt**

```text
/test Generate tests for loading and saving tasks in #file:solutions/lab-03/task_manager.py
```

**Example response**

> Here is a pytest suite that covers loading from a missing file, loading invalid JSON, saving tasks, and round-tripping saved data. I used temporary file setup and monkeypatching to isolate the data file path.

## Advanced — `#file` refactor prompt

**Prompt**

```text
Using #file:lab-03-feature-build/starter/main.py and #file:solutions/lab-03/task_manager.py, suggest a refactor that separates persistence logic from CLI interaction.
```

**Example response**

> A clean refactor would move `load_tasks` and `save_tasks` into a `storage.py` module and keep CLI-only concerns in `main.py`. This reduces responsibility in the CLI entry point and makes persistence easier to test independently.

## Expert — multi-turn build workflow

**Prompt 1**

```text
Add a priority field to tasks and keep the app beginner-friendly.
```

**Example response**

> Start by updating the task model to include a `priority` key with values like `low`, `medium`, or `high`. Then update `add_task` to accept and validate priority input.

**Prompt 2**

```text
Now update the list output to show priorities.
```

**Example response**

> You can include priority in the list line, for example: `[✓] 3: Prepare demo slides (high)`.

**Prompt 3**

```text
Now generate tests for add, list, and persistence behavior with priorities.
```

**Example response**

> I generated tests that verify default priority handling, invalid priority rejection, list formatting, and JSON round-tripping for the new field.

## Reminder

Chat responses will vary by editor, version, and current context. Treat these examples as patterns, not canonical answers.
