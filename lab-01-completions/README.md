# Lab 01 — Practicing Copilot Completions

This lab helps you build confidence with **inline suggestions** in both Python and JavaScript.

## Goal

Learn how Copilot responds to different kinds of context:
- comments
- function names
- parameter names
- type hints / JSDoc
- docstrings

## Files in this lab

- `prompt_practice.py` — Python exercises
- `prompt_practice.js` — JavaScript exercises

## How to trigger Copilot

You usually do not need a special command.

- Start typing code or a descriptive comment
- Pause briefly to let Copilot suggest the next lines
- Press `Tab` to accept a suggestion
- If you do not like the suggestion, keep typing or ask for another one

## Exercises

### 1. Comment-driven completion

Open either file and work through the comment-based prompts.

Expected outcome:
- You should see Copilot suggest a likely function implementation based on your comment and function signature.

### 2. Type-guided completion

Use the functions with type hints or JSDoc already in place.

Expected outcome:
- Suggestions should become more precise because the parameters and return types narrow the problem.

### 3. Docstring-first completion

Read the docstring and let Copilot propose the function body.

Expected outcome:
- The implementation should often align closely with the examples and rules described in the docstring.

## Tips for better completions

- Be specific about the behavior you want
- Use clear function names
- Add type hints or JSDoc where possible
- Mention constraints like “raise ValueError” or “return None if not found”
- Include examples in comments or docstrings when helpful

## Reflection questions

After each exercise, ask yourself:
- Did Copilot understand my intent?
- What context made the suggestion better?
- What would I rewrite to improve the next suggestion?

## If you get stuck

- Rewrite the comment with more detail
- Rename the function to be more explicit
- Add type hints or a docstring
- Compare your work to `../solutions/lab-01/`
