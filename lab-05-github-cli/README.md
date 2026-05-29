# Lab 05 — GitHub Copilot in the CLI

This lab introduces GitHub Copilot CLI: a terminal-first experience that brings AI assistance directly into your command-line workflow.

## Goal

Learn how to:
- Install and authenticate GitHub Copilot in the CLI
- Use `gh copilot suggest` to generate shell commands from natural language
- Use `gh copilot explain` to understand unfamiliar commands
- Use VS Code agent mode for multi-step tasks alongside terminal workflows
- Understand when to use CLI-based Copilot vs. IDE-based Copilot

## Files in this lab

- `exercises/CLI_CHALLENGES.md`

## Background: IDE vs. CLI

| Feature | IDE (VS Code) | CLI (Terminal) |
| --- | --- | --- |
| Inline completions | ✅ Yes | ❌ No |
| Copilot Chat | ✅ Yes | ✅ Via `gh copilot suggest` |
| File and workspace context | ✅ Rich | ⚠️ Limited |
| Shell command generation | ❌ No | ✅ Yes |
| Autonomous multi-step tasks | ✅ In VS Code agent mode | ❌ Not covered by `gh copilot` in this lab |
| Best for | Editing code | Running commands, automation |

## Recommended approach

1. Complete the setup steps in `setup/PREREQUISITES.md` under the GitHub CLI section.
2. Verify that `gh copilot` is working by running a simple `suggest` command.
3. Work through the challenges in order: explain, suggest, and then the VS Code agent mode exercise.

## Tips

- Think of `gh copilot suggest` as Chat for your terminal.
- Use `--target shell` (default) when generating shell commands, or `--target git` for Git commands, or `--target gh` for GitHub CLI commands.
- Review every suggested command before running it.
- Use VS Code agent mode when you want Copilot to plan a multi-step task and pause for your review along the way.

## Good outcomes for this lab

By the end, you should be able to:
- Generate a shell command from a plain English description
- Explain an unfamiliar command before running it
- Use VS Code agent mode to complete a multi-step workflow with Copilot guidance
- Choose the right tool — CLI vs. IDE — for a given task
