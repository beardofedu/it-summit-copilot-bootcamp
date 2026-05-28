"use strict";

async function fetchJson(url) {
  const response = await fetch(url);
  if (!response.ok) {
    throw new Error(`Request failed with status ${response.status}`);
  }
  return response.json();
}

async function waitAndReturn(ms) {
  await new Promise((resolve) => setTimeout(resolve, ms));
  return "done";
}

async function getActiveUsers(users) {
  return users
    .filter((user) => user.active)
    .sort((a, b) => a.name.localeCompare(b.name));
}

function formatOrderSummary(order) {
  return `Order #${order.id} for ${order.customerName}: $${order.total.toFixed(2)}`;
}

function groupTasksByStatus(tasks) {
  return tasks.reduce((groups, task) => {
    const status = task.status;
    if (!groups[status]) {
      groups[status] = [];
    }
    groups[status].push(task);
    return groups;
  }, {});
}

class ShoppingCart {
  constructor() {
    this.items = [];
  }

  addItem(name, price, quantity = 1) {
    this.items.push({ name, price, quantity });
  }

  removeItem(name) {
    const index = this.items.findIndex((item) => item.name === name);
    if (index >= 0) {
      this.items.splice(index, 1);
      return true;
    }
    return false;
  }

  getTotal() {
    return this.items.reduce((total, item) => total + item.price * item.quantity, 0);
  }

  getSummary() {
    const itemCount = this.items.reduce((count, item) => count + item.quantity, 0);
    return `${itemCount} item(s) - total $${this.getTotal().toFixed(2)}`;
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
