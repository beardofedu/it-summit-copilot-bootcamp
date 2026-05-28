# PRESENTER GUIDE — Accelerated Copilot Bootcamp

## Session overview

- **Title:** Accelerated Copilot Bootcamp — Fundamentals to Advanced
- **Duration:** 120 minutes
- **Audience:** Mixed technical and non-technical learners, all skill levels, starting from zero
- **Primary focus:** GitHub Copilot completions + Chat, prompt engineering, practical workflows
- **Format:** Live demos + attendee hands-on labs + Q&A
- **Tech requirements:** VS Code, GitHub Copilot, Copilot Chat, Node.js LTS, Python 3.9+, internet access

## Before You Begin

### Presenter checklist

- [ ] Open this repository in VS Code
- [ ] Verify GitHub Copilot is signed in and active
- [ ] Verify Copilot Chat is available in the editor/sidebar
- [ ] Open the terminal and confirm `python --version` and `node --version`
- [ ] Pre-open these files in tabs:
  - [ ] `README.md`
  - [ ] `lab-01-completions/prompt_practice.py`
  - [ ] `lab-01-completions/prompt_practice.js`
  - [ ] `lab-03-feature-build/starter/main.py`
  - [ ] `lab-04-advanced-chat/exercises/CHAT_CHALLENGES.md`
- [ ] Decide whether you will reveal the `solutions/` directory during the session or only after debrief
- [ ] Have a backup plan if Copilot is temporarily unavailable: use screenshots, prerecorded GIFs, or talk through expected behaviors

### Framing to use at the start

🗣 **Opening setup:**

> Today is about becoming comfortable with GitHub Copilot fast. We are not trying to memorize every feature. We are learning a practical workflow: when inline suggestions are enough, when Chat is better, and how to guide both with better prompts.

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

### Demo `/test`

💻 Select a function or reference a file.

Prompt:

> /test Generate tests for the task loading and saving behavior.

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

---

# Section 5: Q&A & Wrap-up

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
- Reuse the labs in this repo after the session
- Try the same workflows on a real project at work this week

## Suggested Q&A prompts if the room is quiet

🙋 “When should I trust Copilot and when should I double-check it?”

🙋 “What kinds of prompts give you the best results in your day-to-day work?”

🙋 “How do you balance speed with code quality when using AI tools?”

🙋 “What is the difference between asking Chat for a solution vs. asking it for options?”

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
- **Better prompts** = more context, more intent, more constraints
- **Best workflow** = completions for momentum, Chat for reasoning
- **Best facilitation move** = ask attendees what they told Copilot
