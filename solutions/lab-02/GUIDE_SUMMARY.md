# Prompt Engineering Cheat Sheet

## Better prompt formula

**Context + Intent + Constraints = Better Copilot output**

## Quick examples

### Weak

```python
# process data
```

### Better

```python
# Filter the input records to active users only and return their email addresses sorted alphabetically.
```

## Best levers to improve completions

- Use specific function names
- Add type hints or JSDoc
- Write the docstring first
- Include edge cases and output expectations
- Keep prompts short but informative

## Anti-patterns

- vague comments
- generic names like `helper` or `thing`
- missing constraints
- accepting code without review
- trying to solve a multi-step design problem with one tiny inline prompt

## Rule of thumb

- **Completions** for “write the next chunk of code”
- **Chat** for “help me reason about this change”
