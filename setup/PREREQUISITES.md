# Setup & Prerequisites

Please complete this setup before the session starts so you can spend your time learning, not troubleshooting.

## Required tools

### 1. Visual Studio Code

Download and install VS Code:
- https://code.visualstudio.com/

### 2. GitHub Copilot extension

Install the official extension:
- https://marketplace.visualstudio.com/items?itemName=GitHub.copilot

### 3. GitHub Copilot Chat extension

Install the official Chat extension:
- https://marketplace.visualstudio.com/items?itemName=GitHub.copilot-chat

### 4. Node.js LTS

Install the latest LTS version:
- https://nodejs.org/

Verify installation:

```bash
node --version
npm --version
```

### 5. Python 3.9+

Install Python 3.9 or newer:
- https://www.python.org/downloads/

Verify installation:

```bash
python --version
```

> Note: On some systems the command may be `python3` instead of `python`.

## Sign in and enable Copilot

1. Open VS Code.
2. Sign in with your GitHub account if prompted.
3. Confirm that your account has access to GitHub Copilot.
4. Open the Copilot Chat panel to verify it loads.

## Quick Copilot verification test

1. Create a new file named `copilot_test.py`.
2. Paste this comment:

```python
# Function that returns the sum of all even numbers in a list
```

3. Start typing:

```python
def sum_even_numbers(values: list[int]) -> int:
```

4. Pause for a moment.
5. If Copilot is working, you should see a suggested function body.
6. Press `Tab` to accept it.

If that works, you are ready for the session.

## Fork and clone this repository

### Option A: Fork in the browser

1. Open the repository in GitHub.
2. Click **Fork**.
3. Clone your fork:

```bash
git clone https://github.com/YOUR-USERNAME/it-summit-copilot-bootcamp.git
cd it-summit-copilot-bootcamp
code .
```

### Option B: Use GitHub CLI

```bash
gh repo fork beardofedu/it-summit-copilot-bootcamp --clone
cd it-summit-copilot-bootcamp
code .
```

## Recommended VS Code settings

These are optional but helpful:

- Enable **inline suggestions**
- Keep the **Chat** panel easy to access
- Turn on autosave if you like quick iteration
- Make sure Python and JavaScript language support extensions are installed

## Troubleshooting

### Copilot is not showing suggestions

Try the following:
- Confirm you are signed into GitHub in VS Code
- Confirm your account has Copilot access
- Ensure the Copilot extension is enabled for the current workspace
- Restart VS Code
- Open the Command Palette and run **GitHub Copilot: Enable**

### Copilot Chat is missing

- Confirm the Copilot Chat extension is installed
- Reload the VS Code window
- Open the Chat view from the Activity Bar or Command Palette

### Python or Node commands are not found

- Reinstall Python or Node.js
- Restart your terminal after installation
- Verify your system `PATH` is updated correctly

### Suggestions look irrelevant

That is normal sometimes. Improve the context by adding:
- clearer comments
- better function names
- type hints or JSDoc
- a docstring with expected behavior

### Corporate or school environment issues

If you are using a managed machine, extensions or sign-in flows may be restricted. If possible, test on a personal machine before the session.

## Final pre-session checklist

- [ ] VS Code installed
- [ ] Copilot extension installed
- [ ] Copilot Chat extension installed
- [ ] GitHub account signed in
- [ ] Copilot verified with a quick test
- [ ] Node.js LTS installed
- [ ] Python 3.9+ installed
- [ ] Repository forked and cloned
