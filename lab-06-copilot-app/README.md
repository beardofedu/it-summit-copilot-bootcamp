# Lab 06 — GitHub Copilot App

This lab introduces the GitHub Copilot app: a desktop application for agent-driven development that brings parallel workstreams, GitHub integration, and pull request lifecycle management into one place.

## Goal

Learn how to:
- Install and sign in to the GitHub Copilot app
- Start an agent session from a GitHub issue or repository
- Run multiple agents in parallel across different workstreams
- Review agent-proposed changes and create a pull request
- Understand when to use the Copilot app vs. VS Code agent mode vs. CLI

## Files in this lab

- `exercises/APP_CHALLENGES.md`
- `AZURE_BOARDS_REFERENCE.md`

## Background: GitHub Copilot App vs. VS Code agent mode vs. CLI

| Feature | GitHub Copilot App | VS Code agent mode | GitHub Copilot CLI |
| --- | --- | --- | --- |
| Inline completions | ❌ No | ✅ Yes | ❌ No |
| Copilot Chat | ✅ Yes | ✅ Yes | ✅ Via `gh copilot suggest` |
| Parallel workstreams | ✅ Yes | ❌ No | ❌ No |
| GitHub issue / PR integration | ✅ Native | ⚠️ Limited | ✅ Via `gh` |
| File and workspace context | ✅ Full repository | ✅ Open workspace | ⚠️ Limited |
| Shell command generation | ❌ No | ❌ No | ✅ Yes |
| PR lifecycle management | ✅ Yes | ❌ No | ⚠️ Partial |
| Best for | Agent-driven workflows, parallel tasks, PR reviews | Multi-step editor tasks with step-by-step approval | Terminal command generation and explanation |

## Availability

The GitHub Copilot app is currently in **public preview**:

- **Copilot Business and Enterprise** subscribers have access today
- **Copilot Pro and Pro+** subscribers can sign up for early access at [gh.io/github-app](https://gh.io/github-app)

## Prerequisites

- Git installed on your machine
- An active GitHub Copilot subscription (Business, Enterprise, Pro, or Pro+)
- Download the app from [github.com/github/app](https://github.com/github/app)

## Recommended approach

1. Install the app and sign in with your GitHub account.
2. Open a repository you own or have write access to.
3. Work through the challenges in order: start a session, direct the agent, review changes.
4. Review `AZURE_BOARDS_REFERENCE.md` for the Azure DevOps workflow that sends Azure Boards work items to Copilot cloud agent.

## Tips

- Think of the Copilot app as a **control panel for AI agents**. You assign tasks; the agents do the work.
- Use it for tasks that span multiple files or require a full PR workflow, not just a single function.
- The app integrates directly with GitHub, so issues and pull requests appear natively.
- You can run multiple sessions in parallel — use this for independent features or fixes.
- Always review the diff before merging a pull request, just as you would review a teammate's work.

## Good outcomes for this lab

By the end, you should be able to:
- Start an agent session from a repository or GitHub issue
- Direct the agent with a clear task description
- Review proposed file changes in the built-in diff view
- Create or update a pull request from the agent's output
- Explain the difference between the Copilot app, VS Code agent mode, and `gh copilot`
