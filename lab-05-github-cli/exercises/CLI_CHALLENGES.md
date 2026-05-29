# CLI Challenges — GitHub Copilot in the Terminal

Work through these challenges in order. Each builds on the previous one.

## Setup verification

Before starting, confirm your setup is working:

```bash
gh --version
gh copilot --version
```

If either command fails, return to `setup/PREREQUISITES.md` and complete the GitHub CLI section.

---

## Beginner challenge: explain a command

### Use `gh copilot explain` to understand an unfamiliar command

Run the following and read the output:

```bash
gh copilot explain "find . -type f -name '*.log' -mtime +7 -delete"
```

**Goal:**
- See how Copilot breaks down a shell command into plain English
- Build confidence to use `explain` before running commands you didn't write

**Try it yourself:**
Pick any shell command from your history or from a script you've seen and run:

```bash
gh copilot explain "<your command here>"
```

**Reflection questions:**
- Did the explanation make sense?
- Did Copilot catch any risks or side effects?

---

## Beginner challenge: suggest a simple shell command

### Use `gh copilot suggest` to generate a command from natural language

Try this request:

```bash
gh copilot suggest "list all files larger than 100MB in the current directory"
```

Copilot will ask what kind of command you want. Select **shell command**.

**Goal:**
- Generate a useful shell command without knowing the exact syntax
- Review the output before running it

**Try it yourself:**

Generate commands for each of these tasks:

1. "Find all `.py` files changed in the last 24 hours"
2. "Count the number of lines in all JavaScript files recursively"
3. "Show the 5 largest directories in the current path"

**Reflection questions:**
- Did Copilot generate the right command?
- What could you add to the prompt to make the result more precise?

---

## Intermediate challenge: suggest Git commands

### Use `gh copilot suggest` with a Git target

Run:

```bash
gh copilot suggest "undo the last commit but keep the changes staged" --target git
```

**Goal:**
- See how Copilot handles Git-specific commands
- Understand the `--target git` flag

**Try it yourself:**

Generate Git commands for each of these tasks:

1. "Show which files were changed in the last 3 commits"
2. "Create a new branch from main and switch to it"
3. "Stash all changes including untracked files"

**Reflection questions:**
- How does adding `--target git` change the suggestions?
- Did Copilot choose the safest approach for destructive operations like undo?

---

## Intermediate challenge: suggest GitHub CLI commands

### Use `gh copilot suggest` with a GitHub CLI target

Run:

```bash
gh copilot suggest "create a pull request from current branch to main with a draft flag" --target gh
```

**Goal:**
- Use Copilot to learn GitHub CLI commands
- See how `--target gh` scopes suggestions to `gh` subcommands

**Try it yourself:**

Generate `gh` commands for:

1. "List all open pull requests in this repository"
2. "View the latest failed GitHub Actions workflow run"
3. "Clone a repository and open it in VS Code"

---

## Advanced challenge: multi-step automation

### Chain multiple `suggest` calls to build a workflow

Goal: Create a small Bash script that uses Copilot-suggested commands to:
1. Find all Python files modified in the last 7 days
2. Run a linter against them
3. Output a summary file

**Step 1:** Ask Copilot for the find command:

```bash
gh copilot suggest "find Python files modified in the last 7 days"
```

**Step 2:** Ask Copilot for the lint command:

```bash
gh copilot suggest "run flake8 against a list of Python files passed as arguments"
```

**Step 3:** Ask Copilot how to redirect output:

```bash
gh copilot suggest "run a command and save stdout and stderr to a file named summary.txt"
```

**Combine the suggestions** into a small shell script called `lint_recent.sh`.

**Goal:**
- Practice building a real automation from multiple Copilot suggestions
- Get comfortable reviewing and adapting suggested commands

---

## Expert challenge: VS Code agent mode

### Use Copilot agent mode for a multi-step task

In VS Code, agent mode allows Copilot to autonomously plan and execute a sequence of steps to accomplish a complex goal — with your review at each stage.

#### In VS Code (agent mode)

1. Open VS Code in this repository.
2. Open Copilot Chat.
3. Switch to **agent mode** using the mode picker in the Chat panel (look for the model/mode selector).
4. Enter this task:

```text
Review all Python files in lab-03-feature-build/starter/, identify any missing error handling, and propose a fix for each issue found.
```

5. Copilot will plan steps, propose changes, and ask for your approval before applying each one.

**Goal:**
- See Copilot plan and execute a multi-step task
- Practice approving, rejecting, or refining individual steps
- Compare this to what you would do manually

**Reflection questions:**
- Where did Copilot's plan make sense?
- Where did you need to correct its approach?
- How does agent mode compare to running individual `suggest` commands?

---

## Comparison challenge: IDE vs. CLI

Pick one task and try it two ways:

**Task:** "Add a docstring to every function in `solutions/lab-03/task_manager.py` that is missing one."

**Try it in VS Code:**
1. Open Copilot Chat.
2. Reference the file with `#file:solutions/lab-03/task_manager.py`.
3. Prompt: "Add a docstring to every function in this file that is missing one."

**Try it in the terminal:**

```bash
gh copilot suggest "add docstrings to all functions missing them in a Python file"
```

**Compare:**
- Which approach gave more useful output?
- Which was faster to iterate with?
- Which approach was easier to review and apply safely?

**Key takeaway:** IDE Copilot is stronger for file-level edits with rich context. CLI Copilot is stronger for generating and understanding shell, Git, and automation commands.

---

## Reflection questions for the full lab

After finishing the challenges, think about:

- What tasks in your daily workflow would benefit most from `gh copilot suggest`?
- When would you use `gh copilot explain` before running a command?
- How does agent mode change what you delegate vs. what you control?
- What is the right split between terminal-based Copilot and editor-based Copilot in your own work?
