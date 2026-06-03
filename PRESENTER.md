# PRESENTER GUIDE — Accelerated Copilot Bootcamp

## Session overview

- **Title:** Accelerated Copilot Bootcamp — Fundamentals to Advanced
- **Duration:** 140 minutes
- **Audience:** Mixed technical and non-technical learners, all skill levels, starting from zero
- **Primary focus:** GitHub Copilot completions + Chat, prompt engineering, CLI usage, VS Code agent mode, practical workflows
- **Format:** Live demos + attendee hands-on labs + Q&A
- **Tech requirements:** VS Code, GitHub Copilot, Copilot Chat, Node.js LTS, Python 3.9+, GitHub CLI, internet access

## Before You Begin

### Presenter checklist

- [ ] Open this repository in VS Code
- [ ] Verify GitHub Copilot is signed in and active
- [ ] Verify Copilot Chat is available in the editor/sidebar
- [ ] Open the terminal and confirm `python --version` and `node --version`
- [ ] Confirm `gh --version` and `gh copilot --version` in the terminal
- [ ] Pre-open these files in tabs:
  - [ ] `README.md`
  - [ ] `lab-01-completions/prompt_practice.py`
  - [ ] `lab-01-completions/prompt_practice.js`
  - [ ] `lab-03-feature-build/starter/main.py`
  - [ ] `lab-04-advanced-chat/exercises/CHAT_CHALLENGES.md`
  - [ ] `lab-05-github-cli/exercises/CLI_CHALLENGES.md`
  - [ ] `lab-06-copilot-app/exercises/APP_CHALLENGES.md`
- [ ] Decide whether you will reveal the `solutions/` directory during the session or only after debrief
- [ ] Have a backup plan if Copilot is temporarily unavailable: use screenshots, prerecorded GIFs, or talk through expected behaviors

### Framing to use at the start

🗣 **Opening setup:**

> Today is about becoming comfortable with GitHub Copilot fast. We are not trying to memorize every feature. We are learning a practical workflow: when inline suggestions are enough, when Chat is better, and how to guide both with better prompts.

🗣 **Connecting back to this morning's Enterprise session (if attendees were there):**

> "Some of you heard the term *context engineering* this morning — the discipline of staging good inputs for AI to work with. Today is the craft side of that. Every prompt-engineering technique we'll practice is also a context-engineering technique. The framing scales from individual habit to team practice to organizational capability."

🗣 **Expectation setting:**

> You do not need prior Copilot experience. If you are brand new, that is completely fine. We start from zero and build up in layers.

⚠️ **Presenter tip:** Normalize that Copilot is probabilistic.

> Copilot will not give identical output for everyone in the room, and that is okay. The learning goal is not matching my exact code — it is learning how to steer the tool.

---

# Section 1: Copilot Fundamentals & Prompt Engineering

⏱ **20 minutes**

## Section goal

Help attendees understand what Copilot is, how it gets context, and how prompt quality changes suggestion quality.

## Speaker notes

🗣 **What is Copilot?**

- Copilot is an AI coding assistant integrated into the editor.
- The fastest mental model: **autocomplete on steroids**.
- It looks at nearby context such as:
  - the current file
  - comments
  - function names
  - parameter names
  - type hints
  - surrounding code patterns
- It predicts what code is likely to come next.

🗣 **How it works at a high level**

- Copilot does not “understand” your project the way a human does.
- It works by using the context available in the editor and producing likely continuations.
- Better context tends to produce better suggestions.
- Vague prompts often produce vague, generic, or partially useful output.

🗣 **Key message**

> The quality of your prompt directly shapes the quality of the suggestion.

## Key talking points

- Copilot is strongest when the next step is reasonably inferable.
- Comments can act like prompts.
- Function and variable names are powerful hints.
- Type hints and docstrings reduce ambiguity.
- Accepting a suggestion with `Tab` is only the start — review, edit, and guide the next one.

## Demo script: first completion in Python

💻 **Demo setup**

1. Open `lab-01-completions/prompt_practice.py`
2. Scroll to the first exercise.
3. Narrate what you are about to do before typing.

💻 **Suggested demo narration**

> I am going to write a descriptive comment and then pause. Watch what Copilot suggests.

💻 **Type this comment:**

```python
# Function that validates an email address and returns True when the format looks valid
```

💻 **Then type:**

```python
def validate_email(email: str) -> bool:
```

💻 **Pause and let Copilot suggest the body**

- Point out ghost text if visible.
- Accept with `Tab`.
- Briefly review the generated code out loud.

🗣 **What to say while reviewing**

- “This is fast, but I still need to validate it.”
- “Copilot got the intent mostly right because I gave it context: a comment, a function name, a parameter, and a return type.”

## Demo: vague vs. specific prompt

💻 **Vague example**

Type:

```python
# handle input
```

Then start a function like:

```python
def process_input(value):
```

🗣 **Expected teaching point**

- Suggestion will often be generic or arbitrary.
- There is not enough information about validation, data type, expected output, or constraints.

💻 **Specific example**

Replace it with:

```python
# Normalize a user-entered phone number by removing spaces, dashes, and parentheses.
# Return the cleaned digits only if the result has exactly 10 digits; otherwise raise ValueError.
```

Then type:

```python
def normalize_phone_number(raw_value: str) -> str:
```

🗣 **Expected teaching point**

- Better prompt = better output.
- The prompt now contains context, intent, and constraints.

## Prompt engineering basics to teach

🗣 **Practical framework:**

A useful Copilot prompt usually contains:

1. **Context** — what data or domain are we working with?
2. **Intent** — what should this code do?
3. **Constraints** — what rules, edge cases, or formats matter?

### Patterns to highlight

- **Function name hints**
  - `normalize_phone_number` is better than `handle_data`
- **Type hints**
  - `email: str -> bool` narrows the likely implementation
- **Docstring-first approach**
  - Write the docstring before the body to describe expected behavior
- **Examples in comments**
  - If time allows, show that sample inputs and outputs often improve completions

## Transition to hands-on

🧪 **Cue for attendees**

> Your turn. Open `lab-01-completions` and work through the exercises. The goal is not to finish quickly — it is to notice how suggestion quality changes when your prompt gets clearer.

⚠️ **Facilitation tips**

- Encourage attendees to try one vague prompt, then rewrite it.
- Remind them they can partially accept/edit suggestions.
- Walk around and ask: “What information did you give Copilot there?”

---

# Section 2: Transitioning to Chat

⏱ **15 minutes**

## Section goal

Show when inline completions stop being enough and how Chat helps with explanation, planning, debugging, and code transformation.

## Speaker notes

🗣 **Core message**

Inline completions are great when you mostly know what to write next. Chat is better when you need help thinking through the next step.

### When completions are not enough

- You need to understand existing code
- You need a multi-step change
- You want multiple options
- You need debugging help
- You want tests, refactors, or documentation from existing code

🗣 **Bridge statement**

> Completions and Chat are not competing tools. They are a workflow. Completions help you write. Chat helps you think, explain, transform, and iterate.

## Demo: use Chat to explain and extend code

💻 **Demo flow**

1. Keep the Python code you just generated visible.
2. Open Copilot Chat.
3. Ask:

> Explain what this function does and point out any edge cases I should consider.

4. Then follow up with:

> Update this function so it also rejects email addresses with spaces and includes a short docstring.

🗣 **Teaching points during demo**

- Chat can explain code you already wrote.
- Chat can propose improvements.
- You can iterate in multiple turns instead of trying to say everything perfectly at once.

## Key talking point

🗣 **Say this explicitly:**

> Use completions for local momentum. Use Chat when you need reasoning, explanation, or a larger change.

## Transition cue

🧪 **Lead into the larger build**

> In the next lab, we will combine both modes. Use completions for boilerplate and straightforward functions. Use Chat when the logic gets more complex or when you want help checking edge cases.

---

# Section 3: Feature Build Lab

⏱ **50 minutes**

## Section goal

Guide attendees through building a complete but achievable project: a Python Task Manager CLI with JSON persistence.

## Lab transition cue

🧪 **Set the challenge**

> Now we are going from isolated exercises to a realistic feature build. You will create a small application using Copilot for most of the implementation.

## What attendees are building

A **Task Manager CLI** in Python that can:

- add a task
- list tasks
- mark a task complete
- delete a task
- store data in a JSON file
- validate input and handle errors cleanly

## Pacing guidance

- First 10 min: understand the starter file and generate basic structure
- Next 15 min: implement add/list flows
- Next 15 min: implement complete/delete + persistence
- Final 10 min: validate behavior, improve messaging, attempt stretch goals

⚠️ **Presenter tip:** Mention that lab-03 is the centerpiece. If someone only finishes one lab, this is the one to prioritize.

## Facilitation script

🗣 **What to emphasize**

- Start with completions for obvious boilerplate.
- Switch to Chat when you need to reason about file handling, data validation, or command parsing.
- Review every generated block before moving on.

💻 **Suggested prompts to model live**

### For completions

- “I have a function signature and docstring. Let Copilot fill in the body.”
- “I am naming the function clearly so Copilot has better clues.”

### For Chat

- “Using `main.py`, help me implement JSON persistence for this task manager.”
- “Generate a safe way to handle a missing tasks file without crashing.”
- “Refactor this command parsing logic to be easier to read.”

## What to watch for as a facilitator

- Some attendees will over-prompt Chat and underuse completions.
- Others will try to do everything with inline suggestions.
- Encourage a balance:
  - **Completions** for the next chunk of code
  - **Chat** for design, debugging, explanation, and bigger transformations

## Useful coaching questions

- “What did you ask Copilot to do?”
- “Could you make that function name more specific?”
- “Is this a good completions problem or a good Chat problem?”
- “What edge case is missing here?”

## Suggested pacing callouts

🧪 **At ~15 minutes into the lab**

> By now you should have the app structure and at least one command working.

🧪 **At ~30 minutes**

> By now you should be able to add and list tasks, even if the UX is still rough.

🧪 **At ~40 minutes**

> Focus on complete/delete and basic error handling. Stretch goals can wait.

## Tips for facilitating the room

⚠️ **Walk-around tips**

- Help attendees notice when Copilot hallucinates nonexistent helpers.
- Remind them to rerun the app frequently instead of generating a lot of code at once.
- Encourage them to ask Chat for **small, scoped** changes if they are stuck.
- Point out interesting Copilot moments: good variable naming, smart docstring completions, or surprising edge cases it caught.

⚠️ **Time management warning**

If the room is behind schedule, skip stretch goals and move straight to debrief.

---

# Section 4: Slash Commands & Advanced Chat

⏱ **20 minutes**

## Section goal

Give attendees a fast tour of advanced Chat workflows without turning this into a deep feature-by-feature product training.

## Framing statement

🗣

> This section is a sampler. The goal is not mastery of every advanced feature. The goal is awareness: you should leave knowing these tools exist and when to try them.

## Demo plan

### Demo `/explain`

💻 Use a function from `solutions/lab-03/task_manager.py` or attendee code.

Prompt:

> /explain What does this function do? What assumptions is it making?

Talking point:
- Great for onboarding to unfamiliar code

### Demo `/fix`

💻 Intentionally introduce a tiny bug, such as referencing a missing key or mishandling an invalid task ID.

Prompt:

> /fix This command crashes when the user enters a non-numeric task id.

Talking point:
- Useful when you already have an error and want help isolating a repair

### Demo `/tests`

💻 Select a function or reference a file.

Prompt:

> /tests Generate tests for the task loading and saving behavior.

Talking point:
- Helpful for scaffolding tests quickly, but still requires review

### Demo `/doc`

💻 Ask for docs on a function or module.

Prompt:

> /doc Add docstrings for this module and improve the CLI usage text.

Talking point:
- Good for cleanup and polish after logic is working

## File references and scoping

💻 Show `#file` references in Chat

Example prompt:

> Using #file:lab-03-feature-build/starter/main.py, suggest a cleaner way to organize the command handling code.

🗣 **Teaching point**

- `#file` references help scope the conversation and reduce ambiguity.
- This is especially useful in larger repositories.

## Multi-turn conversation demo

💻 Example sequence:

1. “Review this CLI structure and suggest improvements.”
2. “Implement only the persistence changes.”
3. “Now add validation for blank task titles.”
4. “Generate tests for the validation behavior.”

🗣 **Teaching point**

- You do not need the perfect prompt on turn one.
- Chat is strongest as a conversation.

## Advanced tip: `@workspace`

🗣 **Explain briefly**

- `@workspace` can help with whole-project questions.
- Use it when you want broader context across files.

💻 Example prompt:

> @workspace Where is task data loaded, modified, and saved across this project?

⚠️ **Warning to mention**

- Whole-project context can be powerful, but scoped prompts are often faster and more accurate.

## Bridge to Section 5

🗣

> Those slash commands make you *faster*. In the next section we'll touch a different category — slash commands that make you *cheaper*. Under the new credit-based billing, that matters as much as speed. I'll walk through them while you're setting up the CLI lab.

---

# Section 5: GitHub Copilot CLI

⏱ **20 minutes**

## Section goal

Show attendees that GitHub Copilot extends beyond the editor into the terminal, and introduce VS Code agent mode as a way to delegate multi-step tasks.

## Framing statement

🗣

> Everything we have done so far has been inside VS Code. But your terminal is where a lot of real work happens: running builds, writing scripts, using Git, interacting with cloud tools. GitHub Copilot meets you there too.

---

## What is GitHub Copilot in the CLI?

🗣 **Key points to cover**

- The GitHub CLI (`gh`) has a `copilot` extension that adds two main commands:
  - `gh copilot suggest` — generate a shell, Git, or `gh` command from natural language
  - `gh copilot explain` — get a plain-English explanation of an existing command
- It is not inline completions in the terminal. Think of it as **Chat for your shell**.
- It targets three command types via `--target`:
  - `shell` (default) — general shell commands
  - `git` — Git-specific commands
  - `gh` — GitHub CLI commands

## Demo: install and authenticate

💻 **Live demo setup** (if attendees have not done this yet)

Show the install commands and run them live, or refer attendees to `setup/PREREQUISITES.md`.

```bash
gh extension install github/gh-copilot
gh copilot --version
```

🗣 **Say this:**

> If you have a GitHub account with Copilot access, this is all you need for the `gh copilot` exercises in this lab. For newer terminal agent workflows, GitHub is moving toward the standalone GitHub Copilot CLI.

---

## Dead-air narration: cost-aware slash commands

📣 **Use this during install/setup time.** While attendees are running `gh extension install github/gh-copilot`, authenticating, and trying their first commands, walk through these talking points. Treat it as a script — drop any individual command if the room is moving fast.

🗣 **Framing line to open:**

> While you're getting set up, let me give you the other half of the slash command story. The ones you saw in Section 4 made you faster. These five make you cheaper. Two of them — `/chronicle` and `/compact` — work in both the CLI you're installing right now *and* in VS Code Chat. The other three are surface-specific. Either way, the cost-control thinking travels with you. Under credit-based billing as of two days ago, that matters.

### `/usage` — credit accounting in the terminal (~60 sec narration)

🗣
- **CLI only** — does not exist in VS Code Chat.
- Shows your credit consumption directly in the terminal — same information you'd find in the GitHub web UI, available without leaving your shell.
- Suggest attendees run it as their first command once they're authenticated. Sets a baseline for the rest of the lab.

### `/chronicle` — review your session, tune your usage (~2 min narration)

🗣
- Works in **both** Copilot Chat (VS Code) and Copilot CLI.
- Surfaces data points about your recent sessions so you can understand how you're working with Copilot and tweak your usage accordingly.
- Sub-commands worth naming aloud:
  - `/chronicle:standup` — summarize recent sessions by repo and branch
  - `/chronicle:cost-tips` — personalized suggestions on reducing token usage based on your own session history
  - `/chronicle:tips` — general workflow advice
  - `/chronicle:search <query>` — find past sessions
- Closes the loop on the **context engineering** thread from the morning Enterprise session — `/chronicle:cost-tips` surfaces where context engineering decisions are affecting credit spend.

### `/compact` — mid-flight context compression (~90 sec narration)

🗣
- Works in **both** Copilot Chat (VS Code) and Copilot CLI.
- Long conversations carry their full history into every new turn. That history costs tokens, which costs credits.
- `/compact` summarizes the conversation so far and continues with a smaller context footprint.
- Use it when a conversation is productive but getting expensive — preserves the thread without the cost of starting over.

### `/plan` — plan before you spend (~90 sec narration)

🗣
- Available in VS Code Copilot Chat.
- Returns a step-by-step approach **before** any code is generated.
- Front-loads thinking and avoids the failure mode where you burn five turns iterating on the wrong approach.
- Fewer turns to a working result = fewer credits spent.

### `/model` — engine choice as a cost lever (~90 sec narration)

🗣
- Available in VS Code Copilot Chat.
- Different models burn different credits per request. The right model for the task is the first cost decision you make.
- Lighter models for boilerplate, planning, and quick explanations. Reserve premium models for hard reasoning, agent mode, and large refactors.
- Most direct cost lever Copilot gives you in the IDE.

### Cross-surface punchline

🗣

> The cost vocabulary travels across surfaces. `/chronicle` and `/compact` work in both the IDE and the terminal — pick up the discipline once, apply it wherever you're working. Credit-based billing means cost-awareness is a cross-surface discipline, not an IDE-only afterthought.

### Pacing safety net

⚠️ **If the room is mostly through setup already:**
- Drop `/chronicle:tips` and `/plan` first — nice-to-have, not load-bearing.
- Always hit `/usage` (right after install, immediate payoff) and `/chronicle:cost-tips` + `/model` (the UBB moments).
- If only 60 seconds remain, jump to the cross-surface punchline.

⚠️ **If the room is slow on setup:**
- Spend more time on `/chronicle:cost-tips` — show example output if you have a recent session to point at.
- Pivot into Q&A about cost specifically. UBB will dominate the room's questions anyway.

---

## Demo: `gh copilot explain`

💻 **Run this in the terminal**

```bash
gh copilot explain "find . -type f -name '*.log' -mtime +7 -delete"
```

🗣 **Teaching points**

- Copilot breaks the command down flag by flag.
- This is useful when you receive a script you did not write and want to understand it before running it.
- It is a fast way to build your own shell literacy — you learn from the explanation.

💻 **Ask the room:**

> Who has ever run a command copied from the internet without fully understanding it? This is a safer approach.

---

## Demo: `gh copilot suggest` (shell)

💻 **Type this in the terminal:**

```bash
gh copilot suggest "show me all Git branches sorted by the date of their last commit"
```

Select **shell command** when prompted for target type.

🗣 **Teaching points**

- Copilot generates a real, runnable command from plain English.
- It may ask a clarifying question if the request is ambiguous.
- Always review before running — especially commands that modify files or run as root.

💻 **Try a second one:**

```bash
gh copilot suggest "create a pull request from the current branch to main and set me as reviewer" --target gh
```

🗣 **Teaching point**

- The `--target gh` flag scopes the suggestion to GitHub CLI commands.
- Useful for teams adopting `gh` in their workflows.

---

## Demo: `gh copilot suggest` (Git)

💻 **Type this:**

```bash
gh copilot suggest "undo the last commit but keep the changes staged" --target git
```

🗣 **Teaching points**

- Copilot picks the safe approach for destructive Git operations.
- This is especially valuable for developers who are less experienced with Git's more advanced commands.

---

## Comparing CLI and IDE

🗣 **Walk through this comparison live or on a slide:**

| Scenario | Better tool |
| --- | --- |
| Writing or editing code in a file | IDE (VS Code) |
| Generating a shell command | CLI (`gh copilot suggest`) |
| Understanding unfamiliar shell script | CLI (`gh copilot explain`) |
| Debugging a complex function | IDE (Copilot Chat) |
| Running a multi-step Git workflow | CLI (`gh copilot suggest --target git`) |
| Automated multi-step project task | VS Code agent mode |

🗣 **Key message:**

> These tools are not competing. Each one meets you where you already are. If you are in the editor, use Chat. If you are in the terminal, use `gh copilot`. They share the same underlying intelligence.

---

## Demo: VS Code agent mode

🗣 **Introduce agent mode**

> In VS Code, agent mode is what happens when you give Copilot a high-level goal and let it plan and execute the steps, instead of writing one prompt at a time. Think of it like hiring a junior engineer: you give them the goal, you review their work at each step, and you stay in control of what gets applied.

### Agent mode in VS Code

💻 **Live demo flow**

1. Open Copilot Chat in VS Code.
2. Click the mode picker and select **Agent** mode.
3. Enter this task:

```text
Review all Python files in lab-03-feature-build/starter/ and identify any functions missing error handling. For each one found, propose a minimal fix.
```

4. Walk through what Copilot does:
   - It reads the files.
   - It plans a set of changes.
   - It shows each proposed edit before applying.
   - You approve, reject, or refine each step.

🗣 **Teaching points**

- Agent mode is not "set and forget." You are always in the approval loop.
- It is most powerful for tasks with multiple steps across multiple files.
- Think of it as Copilot doing the tedious parts while you focus on review and judgment.

⚠️ **Presenter tip:** If agent mode is not available in your VS Code version, demo this with a multi-turn Chat conversation that mirrors the same workflow manually.

### Knowing when to use agent mode

🗣

> Use agent mode when the task is well-defined but involves too many steps to prompt one by one. Use regular Chat when you want tighter control at each step. Use completions when you mostly know what to write next.

---

## Transition to hands-on

🧪 **Cue for attendees**

> Your turn. Open `lab-05-github-cli/exercises/CLI_CHALLENGES.md` and work through the challenges. If you have GitHub CLI installed and authenticated, start with `explain` and `suggest`. If you do not have it yet, work through the agent mode section in VS Code.

⚠️ **Facilitation tips**

- Walk around and check that attendees have `gh copilot` installed. Some may need to run the install steps during this time.
- The VS Code agent mode challenge works as a fallback if CLI setup is blocked.
- Encourage attendees to try prompts they actually want to know — their real-world use cases are better motivators than practice examples.

---

# Section 6: GitHub Copilot App

⏱ **15 minutes**

## Section goal

Introduce the GitHub Copilot app as a dedicated desktop experience for agent-driven development, and show how it extends the capabilities covered in previous sections into a full PR workflow with parallel workstreams.

## Framing statement

🗣

> Everything we have built toward in this session — completions, Chat, agent mode, CLI — is available piecemeal across different tools. The GitHub Copilot app brings agent-driven development into a single desktop experience built natively on top of GitHub. You get your repositories, issues, and pull requests all in one place, with the ability to run multiple agents in parallel.

---

## What is the GitHub Copilot App?

🗣 **Key points to cover**

- The GitHub Copilot app is a standalone desktop application for **agent-driven development**.
- It is built on top of GitHub Copilot CLI and integrates natively with GitHub.
- Key capabilities:
  - **Parallel workstreams** — run multiple agent sessions at the same time for independent tasks
  - **GitHub-native integration** — repositories, issues, branches, and CI pipelines work out of the box
  - **Full PR lifecycle** — the agent can create, update, and manage pull requests directly from the app
  - **No context switching** — replaces the need to juggle a terminal, an IDE, and browser tabs
- Currently in **public preview**:
  - Copilot Business and Enterprise: available today
  - Copilot Pro and Pro+: sign up for early access at [gh.io/github-app](https://gh.io/github-app)

⚠️ **Presenter tip:** If attendees do not yet have access, run the demo yourself and direct them to sign up afterward. The lab includes a note explaining this.

---

## Demo: start an agent session

💻 **Live demo flow**

1. Open the GitHub Copilot app.
2. Select a repository from the sidebar.
3. Click **New session** and enter a task:

```text
Add a CONTRIBUTING.md file to this repository. Include sections for how to report bugs, how to propose changes, and the pull request process.
```

4. Show the agent planning its steps before making changes.
5. Walk through the **Files** tab to show the diff the agent produced.

🗣 **Teaching points**

- The agent proposes a plan before acting — it is not just making changes blindly.
- You can review and refine each step before accepting.
- This is the same approval-loop principle as VS Code agent mode, but extended across the full GitHub workflow.

---

## Demo: parallel workstreams

💻 **Narrate this concept live (or demo if time allows)**

🗣

> One of the most powerful things about the Copilot app is that you are not limited to one task at a time. You can start a session to write tests on one branch while another session is updating documentation on a different branch — both running simultaneously, both producing pull requests for your review.

Show (or describe):

1. **Session 1:** "Write unit tests for the utility module"
2. **Session 2:** "Update the README to document the new testing workflow"
3. Both appear in the sidebar as active sessions.
4. Each produces its own pull request.

🗣 **Teaching points**

- Parallel sessions work best for **independent, non-conflicting tasks**.
- You are the orchestrator — you decide what runs in parallel and what runs in sequence.
- This shifts your role from "writer of code" to "director of agents."

---

## Comparing the full Copilot ecosystem

🗣 **Walk through this comparison live or on a slide:**

| Scenario | Best tool |
| --- | --- |
| Writing or editing a single function | IDE completions (VS Code) |
| Debugging or refactoring with explanation | Copilot Chat (VS Code) |
| Generating a shell or Git command | GitHub Copilot CLI |
| Multi-step task with step-by-step approval | VS Code agent mode |
| Full PR workflow across multiple files | GitHub Copilot app |
| Running two independent features in parallel | GitHub Copilot app |
| Working from a GitHub issue | GitHub Copilot app |

🗣 **Key message:**

> These tools are layered, not competing. Inline completions are the foundation. Chat adds reasoning. Agent mode adds autonomy. The Copilot app adds the full GitHub lifecycle and parallel scale. You do not have to choose one — you choose the right layer for the task.

---

## Transition to hands-on

🧪 **Cue for attendees**

> If you have access to the GitHub Copilot app, open `lab-06-copilot-app/exercises/APP_CHALLENGES.md` and start with the beginner challenge. If you are still on the waitlist, continue exploring the CLI challenges or try the VS Code agent mode exercise.

⚠️ **Facilitation tips**

- Not everyone will have access yet — this is expected in a public preview. Keep the energy positive about what is coming.
- Focus on the concepts (parallel sessions, PR lifecycle, issue integration) even for attendees who are watching the demo only.
- The comparison table is a useful reference for answering "which tool should I use?" questions.

---

# Section 7: Q&A & Wrap-up

⏱ **15 minutes**

## Suggested closing remarks

🗣

> Today was not about replacing your judgment. It was about increasing your speed and lowering the friction of getting started. The best results come when you combine your context and intent with Copilot’s ability to draft, explain, and iterate quickly.

🗣

> If you remember one thing, remember this: better prompts create better outcomes. Comments, names, type hints, docstrings, and scoped Chat requests all help you guide the tool.

## What attendees should do next

- Keep practicing on small everyday tasks
- Use completions for routine code you already understand
- Use Chat for explanation, debugging, refactoring, and tests
- Install `gh` and `gh copilot` and try it on a real shell task this week
- Try VS Code agent mode on a real project task
- Sign up for or install the GitHub Copilot app and run your first agent session
- Reuse the labs in this repo after the session
- Try the same workflows on a real project at work this week

## Suggested Q&A prompts if the room is quiet

🙋 “When should I trust Copilot and when should I double-check it?”

🙋 “What kinds of prompts give you the best results in your day-to-day work?”

🙋 “How do you balance speed with code quality when using AI tools?”

🙋 “What is the difference between asking Chat for a solution vs. asking it for options?”

🙋 "How does the GitHub Copilot app change the way you think about pull requests and code review?"

## Final reminders

⚠️ **Key cautions to reinforce**

- Copilot output should always be reviewed
- Generated code still needs testing
- Small, precise prompts usually outperform giant vague requests
- Inline suggestions and Chat are complementary, not either/or

## Debrief suggestion

If time remains, show the `solutions/` directory and compare one attendee implementation to the reference version. Focus on:

- different but valid solutions
- prompt quality differences
- how Chat vs. completions were used

---

# Quick presenter cheat sheet

- **Copilot completions** = fast drafting in the editor
- **Copilot Chat** = explanation, transformation, debugging, planning
- **GitHub Copilot CLI** = generate and explain shell, Git, and `gh` commands from the terminal
- **VS Code agent mode** = multi-step task delegation with step-by-step approval
- **GitHub Copilot app** = agent-driven development with parallel workstreams and full PR lifecycle
- **Better prompts** = more context, more intent, more constraints
- **Best workflow** = completions for momentum, Chat for reasoning, CLI for terminal tasks, app for full PR workflows
- **Best facilitation move** = ask attendees what they told Copilot
