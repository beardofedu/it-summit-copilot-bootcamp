# Reference — Integrating Copilot Coding Agent with Azure Boards

Use the Azure Boards GitHub integration to send a work item directly to Copilot cloud agent and generate a draft pull request without leaving Azure DevOps.

## Overview

With the Azure Boards GitHub integration, you can invoke Copilot cloud agent from an Azure Boards work item. Copilot uses the work item details as context, creates code changes in a connected GitHub repository, and opens a draft pull request linked back to the work item.

This is useful when your planning and tracking happen in Azure DevOps, but your code review and merge workflow happen on GitHub.

## Prerequisites

- A GitHub account with access to Copilot through a paid Copilot plan
- Repositories connected to Azure DevOps with Copilot cloud agent enabled

## Installing the Azure Boards app on GitHub

> **Note:** You must be an owner or App manager of the GitHub organization or enterprise to install the Azure Boards app.

1. Open the [Azure Boards app in GitHub Marketplace](https://github.com/marketplace/azure-boards).
2. Choose the GitHub account or organization where you want to install the app.
3. Click **Install**.
4. Select the repositories the Azure Boards app should access.
5. Follow the prompts to configure and authorize the app in Azure DevOps.

The Azure Boards app only needs to be installed once per organization. After that, organization members can connect their GitHub account and use the integration.

## Approving updated app permissions

If Azure Boards is already installed, you may need to approve updated permissions before it can communicate with GitHub Copilot.

1. Go to [GitHub App installations](https://github.com/settings/installations).
2. Find **Azure Boards**.
3. Click **Review request**.
4. Review the updated permissions.
5. Click **Accept new permissions**.

## Creating a pull request from a work item

1. Open the work item in Azure Boards.
2. Click the **Copilot** icon on the work item.
3. Select **Create a pull request with Copilot**.
4. Choose the target **GitHub repository**.
5. Optionally change the base branch.
6. Optionally add extra instructions to guide Copilot.
7. Click **Create**.

Copilot cloud agent will process the work item and create a draft pull request linked back to the Azure Boards item.

## Important context and responsible use

- When a work item is sent to Copilot cloud agent, content from text fields such as the description and reproduction steps is captured as context.
- The last 50 comments on the work item are also included.
- That context is stored in the pull request and is visible to anyone with access to the repository.
- Review the generated pull request carefully before merging.

For more guidance, see:

- [Use Copilot cloud agent responsibly](https://docs.github.com/en/copilot/responsible-use/copilot-cloud-agent)
- [About GitHub Copilot cloud agent](https://docs.github.com/en/copilot/concepts/agents/cloud-agent/about-cloud-agent)
- [Official Azure Boards integration documentation](https://docs.github.com/en/copilot/how-tos/use-copilot-agents/cloud-agent/integrate-cloud-agent-with-azure-boards)
