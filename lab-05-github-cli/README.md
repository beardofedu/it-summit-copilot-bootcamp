# Lab 05 — GitHub Copilot CLI

This lab introduces the standalone **GitHub Copilot CLI**: a terminal-native, fully interactive AI agent that brings the same capabilities as VS Code Chat into your command line. Every prompt is a billed agent session with built-in credit visibility.

## Goal

Learn how to:
- Install and authenticate the standalone GitHub Copilot CLI
- Use `copilot -p "<prompt>"` for one-shot, non-interactive prompts
- Use `copilot -i "<prompt>"` (or just `copilot`) for interactive agent sessions
- Read the AI Credits and token output that prints after every prompt
- Use the cost-aware slash commands (`/usage`, `/chronicle`, `/compact`) inside an interactive session
- Use VS Code agent mode for IDE-side multi-step tasks
- Understand when to reach for the CLI agent vs. the IDE agent

## Heads up: `gh copilot suggest`/`explain` is being deprecated

The older `gh copilot` extension (the `gh copilot suggest` and `gh copilot explain` commands) is being replaced by this standalone CLI. On newer installations, running `gh copilot suggest "..."` or `gh copilot explain "..."` will print an error along the lines of `Did you mean: copilot -i "..."?` — that is the migration in progress, not a bug. This lab uses the new standalone CLI throughout.

## Files in this lab

- `exercises/CLI_CHALLENGES.md`

## Background: CLI agent vs. IDE Chat

| Feature | IDE (VS Code Chat) | CLI (Standalone `copilot`) |
| --- | --- | --- |
| Inline code completions | ✅ Yes | ❌ No |
| Interactive multi-turn chat | ✅ Yes | ✅ Yes (`copilot -i`) |
| One-shot non-interactive prompt | ⚠️ Limited | ✅ Yes (`copilot -p`) |
| File and workspace context | ✅ Rich, automatic | ✅ Via `--add-dir` and in-session tools |
| Shell command generation and execution | ⚠️ Indirect | ✅ Native |
| Per-prompt credit visibility | ❌ Use `/usage` to check | ✅ Printed after every `-p` and `-i` turn |
| Slash commands `/usage` | ❌ Not available | ✅ Yes |
| Slash commands `/chronicle`, `/compact` | ✅ Yes | ✅ Yes |
| Slash commands `/model`, `/plan` | ✅ Yes | ❌ Not available |
| Autonomous multi-step tasks | ✅ Agent mode | ✅ Default behavior |
| Best for | Editing code with full IDE review UX | Terminal-native workflows, scripting, cost-aware sessions |

## Recommended approach

1. Complete the setup steps in `setup/PREREQUISITES.md` under the GitHub Copilot CLI section. The install is one command: `npm install -g @github/copilot`.
2. Verify the install by running `copilot --version`. On first run of `copilot` or `copilot -i`, you'll be prompted to authenticate via your browser.
3. Run `/usage` as your first interactive command to set a credit baseline you can compare against at the end of the lab.
4. Work through the challenges in order: `copilot -p` non-interactive, `copilot -i` interactive, then the VS Code agent mode exercise.

## Tips

- **Watch the credit and token line that prints after every `-p` prompt.** It's labeled `AI Credits X.X (Ys)` and `Tokens ↑X • ↓Y`. That's the cost story made literal — you see exactly what each prompt cost.
- For quick, cheap explanations, lower the reasoning effort: `copilot -p --effort low "..."`.
- Inside an interactive session, run `/compact` if the conversation has been productive but is getting long. It summarizes the prior turns and continues with a smaller context footprint.
- Use `/chronicle:cost-tips` to get personalized advice based on your own session history.
- For VS Code agent mode, prefer well-scoped tasks ("review these three files for X") over open-ended goals ("clean up this codebase") — the review loop scales better.

## Good outcomes for this lab

By the end, you should be able to:
- Install and authenticate the standalone GitHub Copilot CLI on your machine
- Run a one-shot prompt with `copilot -p` and read the per-prompt credit cost
- Start an interactive session with `copilot -i`, iterate over multiple turns, and exit cleanly
- Use at least two cost-aware slash commands inside a session (`/usage` plus one of `/chronicle`, `/compact`)
- Run a multi-step VS Code agent mode task with appropriate approval gates
- Articulate when you would reach for the CLI agent vs. the IDE agent for a given task
