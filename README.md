# Accelerated Copilot Bootcamp — Fundamentals to Advanced

Welcome to the repository for the **IT Summit conference session** on GitHub Copilot. This repo is designed for both presenters and attendees: it includes a complete talk track, setup guidance, hands-on labs, and reference solutions.

## Who this bootcamp is for

This session is for **mixed technical and non-technical audiences** and assumes **no previous GitHub Copilot experience**. We start from zero, explain the basics clearly, and build confidence through guided practice.

## Learning objectives

By the end of the session, attendees should be able to:

- Use **Copilot completions** to speed up routine coding tasks
- Use **Copilot Chat** for more complex, multi-step development work
- Understand when to use **inline suggestions vs. Chat**
- Write better prompts using comments, function names, type hints, and docstrings
- Use **GitHub Copilot CLI** to generate and explain shell commands from the terminal
- Use **VS Code agent mode** to delegate multi-step tasks to Copilot
- Build confidence with realistic coding scenarios they can reuse at work

## Prerequisites

Please complete the setup steps before the session:

- [Setup and prerequisites](./setup/PREREQUISITES.md)

You will need:
- VS Code
- GitHub Copilot and Copilot Chat enabled
- Node.js LTS
- Python 3.9+
- A GitHub account with repository access and fork permissions
- GitHub CLI (`gh`) with the Copilot extension installed

## Session agenda

| Time | Topic |
| --- | --- |
| 20 min | Copilot fundamentals and prompt engineering basics |
| 15 min | Transitioning to Copilot Chat for complex tasks |
| 50 min | Hands-on lab: building a feature using both tools |
| 20 min | Slash commands and advanced Chat features |
| 20 min | GitHub Copilot CLI: suggest, explain, and VS Code agent mode |
| 15 min | GitHub Copilot app: agent-driven development and parallel workstreams |
| 15 min | Q&A |

## Lab directory map

- [`demo-app/`](./demo-app/) — **sample application** used by the presenter across all demo sections (Contact Book CLI)
- [`lab-01-completions/`](./lab-01-completions/) — practice getting better inline suggestions in Python and JavaScript
- [`lab-02-prompt-engineering/`](./lab-02-prompt-engineering/) — learn how prompt quality changes Copilot output
- [`lab-03-feature-build/`](./lab-03-feature-build/) — build a complete Python Task Manager CLI using completions and Chat
- [`lab-04-advanced-chat/`](./lab-04-advanced-chat/) — explore slash commands, file references, and multi-turn Chat workflows
- [`lab-05-github-cli/`](./lab-05-github-cli/) — use GitHub Copilot CLI to suggest and explain commands, and practice VS Code agent mode
- [`lab-06-copilot-app/`](./lab-06-copilot-app/) — use the GitHub Copilot app for agent-driven development and parallel workstreams
- [`solutions/`](./solutions/) — reference implementations and example outputs
- [`setup/`](./setup/) — environment preparation and troubleshooting
- [`PRESENTER.md`](./PRESENTER.md) — detailed presenter talk track and demo guidance

## How to use this repo

### Attendees

1. **Fork this repository** to your own GitHub account.
2. **Clone your fork** locally.
3. Open the repo in VS Code.
4. Work through the labs **in order**:
   - Lab 01 → inline completions
   - Lab 02 → prompt engineering
   - Lab 03 → feature build
   - Lab 04 → advanced Chat
   - Lab 05 → GitHub Copilot CLI
   - Lab 06 → GitHub Copilot app
5. Compare your work with the files in [`solutions/`](./solutions/) if you get stuck or want a reference.

### Presenters

- Use [`PRESENTER.md`](./PRESENTER.md) as your talk track.
- Use the labs live during demos or direct attendees into the right folder at each transition.
- Keep the solutions hidden until debrief time if you want attendees to stay hands-on.

## Suggested fork workflow

```bash
gh repo fork beardofedu/it-summit-copilot-bootcamp --clone
cd it-summit-copilot-bootcamp
code .
```

Or fork from the GitHub UI and clone your fork manually.

## Resources

- [GitHub Copilot documentation](https://docs.github.com/copilot)
- [Prompting GitHub Copilot effectively](https://docs.github.com/en/copilot/using-github-copilot/prompt-engineering-for-github-copilot)
- [GitHub Copilot Chat overview](https://docs.github.com/en/copilot/github-copilot-chat/about-github-copilot-chat)
- [VS Code GitHub Copilot extension](https://marketplace.visualstudio.com/items?itemName=GitHub.copilot)
- [VS Code GitHub Copilot Chat extension](https://marketplace.visualstudio.com/items?itemName=GitHub.copilot-chat)
- [GitHub Copilot in the CLI](https://docs.github.com/en/copilot/github-copilot-in-the-cli/about-github-copilot-in-the-cli)
- [GitHub CLI installation](https://cli.github.com/)
- [VS Code agent mode](https://code.visualstudio.com/docs/copilot/agents/overview)
- [GitHub Copilot app](https://github.com/github/app)

Enjoy the bootcamp — and remember that the goal is not just to use Copilot faster, but to use it **more intentionally**.
