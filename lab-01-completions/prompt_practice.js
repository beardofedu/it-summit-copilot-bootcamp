/*
Copilot completion practice in JavaScript.

Instructions:
1. Read the prompt above each exercise.
2. Put your cursor inside the function or class.
3. Let Copilot suggest the implementation.
4. Review and edit as needed.
*/

// ------------------------------------------------------------
// Section 1: Comment-driven completion for async functions
// ------------------------------------------------------------

// Exercise: Async function that fetches JSON from a URL and throws
// a helpful error if the response is not ok.
async function fetchJson(url) {
  throw new Error("TODO: use Copilot to implement fetchJson");
}

// Exercise: Async function that waits for a given number of milliseconds
// and then resolves with the message "done".
async function waitAndReturn(ms) {
  throw new Error("TODO: use Copilot to implement waitAndReturn");
}

// Exercise: Async function that filters a list of users and returns only
// the active users sorted alphabetically by name.
async function getActiveUsers(users) {
  throw new Error("TODO: use Copilot to implement getActiveUsers");
}

// ------------------------------------------------------------
// Section 2: JSDoc-guided completion
// ------------------------------------------------------------

/**
 * Create a summary string for an order.
 * @param {{ id: number, customerName: string, total: number }} order
 * @returns {string}
 */
function formatOrderSummary(order) {
  throw new Error("TODO: use Copilot to implement formatOrderSummary");
}

/**
 * Group tasks by status.
 * @param {{ title: string, status: string }[]} tasks
 * @returns {Record<string, { title: string, status: string }[]>}
 */
function groupTasksByStatus(tasks) {
  throw new Error("TODO: use Copilot to implement groupTasksByStatus");
}

// ------------------------------------------------------------
// Section 3: Class skeleton
// ------------------------------------------------------------

class ShoppingCart {
  constructor() {
    this.items = [];
  }

  // Add an item with name, price, and quantity.
  addItem(name, price, quantity = 1) {
    throw new Error("TODO: use Copilot to implement addItem");
  }

  // Remove the first item whose name matches.
  removeItem(name) {
    throw new Error("TODO: use Copilot to implement removeItem");
  }

  // Return the total cost of all items.
  getTotal() {
    throw new Error("TODO: use Copilot to implement getTotal");
  }

  // Return a user-friendly summary string.
  getSummary() {
    throw new Error("TODO: use Copilot to implement getSummary");
  }
}

module.exports = {
  ShoppingCart,
  fetchJson,
  formatOrderSummary,
  getActiveUsers,
  groupTasksByStatus,
  waitAndReturn,
};
