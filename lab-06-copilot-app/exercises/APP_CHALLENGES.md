# App Challenges — GitHub Copilot App

Work through these challenges in order. Each one builds on the previous.

> **Note:** The GitHub Copilot app is in public preview. If you do not yet have access, read through the challenges and follow along with the presenter demo. You can sign up for early access at [gh.io/github-app](https://gh.io/github-app).

---

## Setup verification

Before starting, confirm the app is installed and signed in:

1. Open the GitHub Copilot app on your machine.
2. Sign in with your GitHub account if prompted.
3. Verify that at least one repository appears in the sidebar.

If the app is not installed, download it for your platform from [github.com/github/app](https://github.com/github/app):

- Windows (x64 or ARM)
- Mac (Apple Silicon or Intel)
- Linux (AppImage)

---

## Beginner challenge: start your first agent session

### Open a repository and start a session

1. In the GitHub Copilot app, click **New session** or select a repository from the sidebar.
2. Choose a repository you own or have write access to.
3. In the session input box, enter a simple, well-scoped task:

```text
Add a README.md to this repository that describes the project, how to install it, and how to run it.
```

4. Submit the task and watch the agent plan its steps.

**Goal:**
- Observe how the agent interprets your task and proposes a plan before making changes
- See the agent create or edit files in the diff view

**Reflection questions:**
- Did the agent ask any clarifying questions before starting?
- How did it decide what to include in the README?
- What would you change about the prompt to get a better result?

---

## Beginner challenge: review agent-proposed changes

### Inspect the diff before accepting

After the agent proposes changes in the previous challenge:

1. Click the **Files** or **Changes** tab to review the diff.
2. Look at what was added, modified, or removed.
3. If the output is not quite right, send a follow-up message:

```text
The README is missing a "Contributing" section. Please add one with guidance on how to open a pull request.
```

4. Review the updated diff.

**Goal:**
- Practice reviewing proposed changes before accepting them
- Learn how to refine the agent's output with follow-up messages

**Reflection questions:**
- Is the agent's output accurate? Does anything need to be corrected?
- How is reviewing the agent's diff similar to reviewing a teammate's pull request?

---

## Intermediate challenge: create a pull request from agent output

### Turn agent changes into a pull request

1. Start a new session in a repository where you have push access.
2. Give the agent a task that involves code changes:

```text
Add input validation to the existing contact form handler. Validate that the email field contains a valid email address format and that the name field is not empty. Return a 400 error with a descriptive message for each violation.
```

3. Review the proposed changes.
4. When satisfied, use the **Create pull request** button or flow in the app to open a PR.
5. Review the pull request title and description that the agent generated.

**Goal:**
- Complete a full agent workflow: task → changes → pull request
- See how the app integrates with GitHub's pull request lifecycle

**Reflection questions:**
- Did the agent generate a useful PR title and description?
- What would you edit before requesting a review from a teammate?

---

## Intermediate challenge: work from a GitHub issue

### Start a session directly from an issue

1. In the app's **My Work** panel, find an open issue in one of your repositories, or create a new issue first:
   - Go to your repository on GitHub.com and create an issue titled: `Add logging to the main script`
2. Open the issue in the Copilot app.
3. Start an agent session from the issue by selecting **Open in Copilot** or **Start session from issue**.
4. The agent should use the issue title and description as its initial context. Review what it proposes.

**Goal:**
- Experience the GitHub-native integration between issues and agent sessions
- See how a well-written issue title improves the agent's initial plan

**Reflection questions:**
- Did the agent's plan match what you expected from the issue?
- What details in the issue title or body made the agent's output better or worse?

---

## Advanced challenge: run parallel workstreams

### Start two independent sessions at the same time

1. Open the GitHub Copilot app.
2. Start **Session 1** in a repository with the following task:

```text
Write unit tests for the utility functions in the project. Cover at least three functions with multiple test cases each.
```

3. Without waiting for Session 1 to finish, start **Session 2** in the same (or a different) repository:

```text
Update the project's README to include a "Testing" section that explains how to run the test suite.
```

4. Monitor both sessions from the sidebar.
5. Review the output from each session when they complete.

**Goal:**
- Experience parallel workstream management — one of the key advantages of the Copilot app
- See how two independent tasks can run simultaneously

**Reflection questions:**
- How does running tasks in parallel change your workflow compared to doing them one at a time?
- Were there any conflicts between the two sessions' changes?
- What kinds of tasks are good candidates for parallel sessions?

---

## Advanced challenge: compare the tools

### Choose the right Copilot tool for the job

For each scenario below, decide whether you would use the **GitHub Copilot app**, **VS Code agent mode**, or **GitHub Copilot CLI**. Then try the one you chose.

| Scenario | Your choice | Why? |
| --- | --- | --- |
| Fix a bug in a single function while editing code | | |
| Generate a Git command to cherry-pick a range of commits | | |
| Build a new feature across five files and open a PR | | |
| Explain an unfamiliar shell script before running it | | |
| Run two independent feature branches simultaneously | | |

**After completing at least one scenario:**

1. Write down which tool you chose and why.
2. Compare your answers with a neighbor.

**Reflection questions:**
- Which tool felt most natural for your day-to-day work?
- Are there workflows in your current projects that would benefit from parallel agent sessions?
- How does the Copilot app change your relationship with pull requests?

---

## Reflection questions for the full lab

After finishing the challenges, think about:

- What is the difference between directing an AI agent and writing code yourself?
- When is it faster to give a task to the Copilot app than to open VS Code and write it yourself?
- How do you maintain code quality when the agent is doing the typing?
- What does your review process look like when an agent creates a pull request?
- How would you explain the GitHub Copilot app to a non-technical teammate?
