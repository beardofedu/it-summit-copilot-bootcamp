# Prompting Guide for GitHub Copilot

## The anatomy of a good prompt

A strong prompt usually includes three parts:

1. **Context** — what kind of data or problem is this?
2. **Intent** — what should the code accomplish?
3. **Constraints** — what rules, edge cases, or output format matter?

### Example

**Weak:**

```python
# process data
```

**Better:**

```python
# Convert a list of order dictionaries into a summary report.
# Include only orders with status "paid" and return the total revenue as a float.
```

## Comment strategies

### Single-line comments

Best when the task is simple and narrow.

```python
# Return True if the username contains only letters, numbers, and underscores.
```

### Multi-line comments

Best when the task has rules, examples, or edge cases.

```python
# Parse a CSV row into a dictionary using the provided field names.
# Trim whitespace around each value.
# If there are fewer values than field names, fill the missing values with an empty string.
```

## Use function names and parameter names as hints

Names act like prompts.

**Less helpful:**

```python
def handle(data):
```

**More helpful:**

```python
def calculate_monthly_revenue(order_totals: list[float]) -> float:
```

## Type hints and return types as guardrails

The more structure you provide, the less Copilot has to guess.

```python
def find_user(users: list[dict[str, str]], email: str) -> Optional[dict[str, str]]:
```

This gives Copilot clues about:
- expected inputs
- expected output shape
- whether missing values are allowed

## The docstring-first pattern

When the behavior is more detailed, write the docstring before the code.

```python
def normalize_tag(tag: str) -> str:
    """Return a lowercase tag with spaces replaced by hyphens.

    Raise ValueError if the tag is empty after trimming whitespace.
    """
```

Copilot can often generate a better implementation when the contract is already written.

## Bad vs. good prompts

| Bad prompt | Better prompt |
| --- | --- |
| `# process data` | `# Filter the input records to only active users and return their email addresses in alphabetical order.` |
| `# do the thing` | `# Send a password reset email and return False if the user account does not exist.` |
| `# helper function` | `# Helper function that converts cents to a currency string like $12.50.` |
| `# fix the issue` | `# Handle the case where the JSON file is missing by returning an empty task list instead of crashing.` |

## Five anti-patterns to avoid

1. **Being vague**
   - Example: `# process data`
   - Problem: There is no clear goal.

2. **Hiding constraints**
   - Example: forgetting to mention sorting, filtering, or validation rules
   - Problem: Copilot fills in the blanks with guesses.

3. **Using generic names**
   - Example: `data`, `value`, `thing`, `helper`
   - Problem: Weak names weaken the prompt.

4. **Prompting too late**
   - Writing the code skeleton first and only later clarifying the intent
   - Problem: Earlier context could have improved the whole suggestion chain.

5. **Accepting without reviewing**
   - Problem: Good prompting improves output, but does not remove the need for human review.

## Prompt improvement checklist

Before you rely on a suggestion, ask:
- Did I describe the task clearly?
- Did I say what the input and output should look like?
- Did I mention edge cases or constraints?
- Is the function name specific?
- Would a docstring help here?

Good prompting is not about writing long prompts. It is about writing **useful context**.
