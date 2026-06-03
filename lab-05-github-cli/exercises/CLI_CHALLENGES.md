# CLI Challenges — GitHub Copilot CLI (Standalone)

Work through these challenges in order. Each builds on the previous one.

> **Note:** This lab uses the new standalone GitHub Copilot CLI (`copilot`), not the older `gh copilot` extension. If you run `gh copilot suggest` or `gh copilot explain` and get a `Did you mean: copilot -i "..."?` error, that's the deprecation in progress — use the commands below instead.

## Setup verification

Before starting, confirm your setup is working:

```bash
gh --version
copilot --version
```

If `copilot` is not installed, run:

```bash
npm install -g @github/copilot
```

The first time you run `copilot` or `copilot -i`, you'll be prompted to authenticate with your GitHub account via your browser. Complete that flow once before continuing.

---

## Beginner challenge: explain a command with `copilot -p`

### Use `copilot -p` to understand an unfamiliar command

`copilot -p` is **non-interactive mode** — it takes your prompt, answers, and exits. Great for quick lookups and scripts.

Run the following and read the output:

```bash
copilot -p "explain what this shell command does: find . -type f -name '*.log' -mtime +7 -delete"
```

**Watch the bottom of the output.** You'll see a line like:

```
AI Credits 16.2 (4s)
Tokens     ↑ 25.6k • ↓ 52
```

That's the per-prompt cost. Every `-p` invocation prints this — credit-based billing is visible in real time.

**Goal:**
- See how Copilot breaks down a shell command into plain English
- Build confidence to use `copilot -p` before running commands you didn't write
- Notice the credit/token line — that's the cost of this explanation

**Try it yourself:**

Pick any shell command from your history or from a script you've seen and run:

```bash
copilot -p "explain what this command does: <your command here>"
```

For a cheaper, faster explanation, try lowering the reasoning effort:

```bash
copilot -p --effort low "explain what this shell command does: tar xzf foo.tar.gz"
```

Compare the credit cost between the default and `--effort low`.

**Reflection questions:**
- Did the explanation make sense?
- Did Copilot catch any risks or side effects?
- How much did the prompt cost (credits/tokens)?
- How much did `--effort low` reduce the cost? Was the answer still good enough?

---

## Beginner challenge: generate a command with `copilot -p`

### Use `copilot -p` to generate a shell command from natural language

```bash
copilot -p "give me the shell command to list all files larger than 100MB in the current directory"
```

**Goal:**
- Generate a useful shell command without knowing the exact syntax
- Always review the suggested command before running it

**Try it yourself:**

Generate commands for each of these tasks:

1. "Find all `.py` files changed in the last 24 hours"
2. "Count the number of lines in all JavaScript files recursively"
3. "Show the 5 largest directories in the current path"

**Reflection questions:**
- Did Copilot generate a correct, runnable command?
- What could you add to the prompt to make the result more precise?
- What was the credit cost per prompt? Add them up — what did this entire exercise cost?

---

## Intermediate challenge: interactive session with `copilot -i`

### Start an interactive agent session

`copilot -i` (or just `copilot` with no args) opens a **stateful, multi-turn agent session**. The session remembers earlier turns, can read files, can propose and (with your approval) run commands.

Start a session with an opening prompt:

```bash
copilot -i "I need to undo the last commit in this repo but keep the changes staged. Walk me through the safest way."
```

**Inside the session:**

1. Read the response. The agent may ask a clarifying question or propose a command.
2. If it proposes a command, review it before approving.
3. Run `/usage` to see your current credit balance.
4. Send a follow-up turn (just type and press Enter):
   > Now show me how to undo the last 3 commits while preserving all changes in a single working tree.
5. Notice that the agent remembers the prior turn — you didn't have to repeat the repo context.
6. Run `/compact` to summarize the conversation and continue with a smaller context footprint.
7. Send one more follow-up turn and notice the response still has continuity.
8. Exit with `/exit` or Ctrl+D.

**Goal:**
- Experience the difference between a one-shot `-p` prompt and a stateful `-i` session
- Use `/usage` to see real-time credit consumption
- Use `/compact` to manage context cost mid-session

**Reflection questions:**
- How was the multi-turn behavior different from `-p`?
- What did `/usage` show before and after the session?
- Did `/compact` change how the next turn felt? Was the continuity preserved?

---

## Intermediate challenge: chronicle your sessions

### Use `/chronicle` to review past work

Inside an interactive session, run:

```
/chronicle:standup
```

Then try:

```
/chronicle:cost-tips
```

**Goal:**
- See how the CLI surfaces data about your prior sessions
- Get personalized advice on reducing token usage based on your own history
- Understand that `/chronicle` works in both the CLI **and** in VS Code Chat — the cost vocabulary travels across surfaces

**Reflection questions:**
- What patterns did `/chronicle:cost-tips` flag?
- Would any of the suggestions change how you'd run your next session?

---

## Advanced challenge: build a small automation in a single session

### Iteratively build a shell script with `copilot -i`

Start a fresh interactive session:

```bash
copilot -i "I want to build a small Bash script. Don't write code yet — first, suggest the steps."
```

Then in the session, work through these turns one at a time:

1. > "The script should find all Python files modified in the last 7 days, run flake8 against them, and save stdout and stderr to a file named summary.txt. What's a good structure?"
2. > "OK, write the script. Call it lint_recent.sh."
3. > "Add error handling for the case where flake8 is not installed."
4. > "Add a short usage comment at the top."

Approve each proposed file edit if you want the agent to write the file directly, or copy the code into a file yourself.

**Goal:**
- Practice building a real automation through iterative conversation
- See how the agent uses earlier context (the requirements you set in turn 1) without you having to repeat them
- Get comfortable with the approval loop for file edits and command execution

**Reflection questions:**
- How did multi-turn iteration compare to trying to get everything from a single `-p` prompt?
- How many credits did the whole session cost? Was it worth it for a working script?

---

## Expert challenge: VS Code agent mode

### Use Copilot agent mode for a multi-step task in the IDE

In VS Code, agent mode is the IDE-side counterpart to `copilot -i` — same agentic capabilities, different review UX (inline diffs, side-by-side approvals).

1. Open VS Code in this repository.
2. Open Copilot Chat.
3. Switch to **agent mode** using the mode picker in the Chat panel (look for the mode selector).
4. Enter this task:

```text
Review all Python files in lab-03-feature-build/starter/, identify any functions missing error handling, and propose a minimal fix for each issue found.
```

5. Copilot will plan steps, propose changes, and ask for your approval before applying each one.

**Goal:**
- See agent mode plan and execute a multi-step task in the editor
- Practice approving, rejecting, or refining individual proposed edits
- Compare the IDE review UX to the terminal review UX in `copilot -i`

**Reflection questions:**
- Where did the agent's plan make sense? Where did you need to correct it?
- How did the inline diff review feel compared to terminal approvals?
- For this kind of multi-file task, would you reach for VS Code agent mode or `copilot -i` next time? Why?

---

## Comparison challenge: CLI agent vs. IDE Chat for the same task

Pick one task and try it two ways.

**Task:** "Add a docstring to every function in `solutions/lab-03/task_manager.py` that is missing one."

**Try it in VS Code Chat:**
1. Open Copilot Chat in VS Code.
2. Reference the file with `#file:solutions/lab-03/task_manager.py`.
3. Prompt: "Add a docstring to every function in this file that is missing one."
4. Review the proposed edits in the inline diff UX.

**Try it in the CLI agent:**

```bash
copilot -i "Read solutions/lab-03/task_manager.py. Add a docstring to every function in that file that is missing one. Show me the diff before applying."
```

Approve or reject the proposed edits as they come.

**Compare:**
- Which approach gave more useful output?
- Which was faster to iterate with?
- Which felt easier to review and apply safely?
- Which cost more credits? (Check with `/usage` mid-session in the CLI; check the GitHub web UI for IDE Chat.)

**Key takeaway:** Both surfaces share the same engine, the same credits, and the same multi-turn agent capabilities. The right choice usually comes down to "where is my work already?" — if you're editing in VS Code, stay there. If you're in the terminal running scripts and Git commands, the CLI agent meets you there.

---

## Reflection questions for the full lab

After finishing the challenges, think about:

- What tasks in your daily workflow would benefit most from `copilot -p`? From `copilot -i`?
- How did seeing the credit/token line after every `-p` prompt change how you thought about cost?
- Which slash commands (`/usage`, `/chronicle:cost-tips`, `/compact`) felt most useful, and which felt like overkill?
- For a long, exploratory session, when would you compact? When would you start a fresh session with `/new` instead?
- What is the right split between terminal-based Copilot and editor-based Copilot in your own work?
