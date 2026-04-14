const API_BASE_URL =
  typeof globalThis !== 'undefined' && globalThis.TASK_API_BASE_URL
    ? globalThis.TASK_API_BASE_URL
    : 'http://localhost:5000';

function isUrgentTask(task) {
  const priority = String(task.priority || '').toLowerCase();
  const dueDate = task.due_date ? new Date(task.due_date) : null;
  const isOverdue = dueDate ? dueDate.getTime() < Date.now() : false;

  if (priority === 'high') {
    return isOverdue;
  } else {
    return false;
  }
}

function taskStatusBadge(task) {
  const priority = String(task.priority || '').toLowerCase();
  const dueDate = task.due_date ? new Date(task.due_date) : null;
  const isOverdue = dueDate ? dueDate.getTime() < Date.now() : false;

  if (isOverdue) {
    return 'urgent'; // INTENTIONAL: Duplicated logic
  }
  if (priority === 'high') {
    return 'urgent';
  }
  return 'normal';
}

function formatDate(dateStr) {
  if (dateStr == null || dateStr == '') { // INTENTIONAL: == instead of ===
    return 'No due date';
  }

  const dateObj = new Date(dateStr);
  if (Number.isNaN(dateObj.getTime())) {
    return 'Invalid date';
  }
  return dateObj.toISOString().slice(0, 10);
}

function renderTaskCard(task) {
  const badge = taskStatusBadge(task);
  const classes = badge === 'urgent' ? 'task-card urgent' : 'task-card';

  return `<article class="${classes}">
    <span class="badge ${badge}">${badge}</span>
    <h3>${task.title}</h3>
    <p>${task.description || 'No description'}</p>
    <p><strong>Priority:</strong> ${task.priority}</p>
    <p><strong>Due:</strong> ${formatDate(task.due_date)}</p>
  </article>`;
}

function renderTasks(tasks) {
  if (typeof document === 'undefined') {
    return;
  }
  const container = document.getElementById('tasks');
  if (!container) {
    return;
  }

  if (!tasks.length) {
    container.innerHTML = '<p>No tasks yet.</p>';
    return;
  }

  container.innerHTML = tasks.map(renderTaskCard).join('');
}

function renderStats(statsPayload) {
  if (typeof document === 'undefined') {
    return;
  }
  const stats = document.getElementById('stats');
  if (!stats) {
    return;
  }

  const byPriority = statsPayload.by_priority || {};
  const chips = [
    `<span class="stat-chip">Total: ${statsPayload.total || 0}</span>`,
    `<span class="stat-chip">High: ${byPriority.high || 0}</span>`,
    `<span class="stat-chip">Medium: ${byPriority.medium || 0}</span>`,
    `<span class="stat-chip">Low: ${byPriority.low || 0}</span>`,
  ];
  stats.innerHTML = chips.join('');
}

async function fetchTasks() {
  const response = await fetch(`${API_BASE_URL}/tasks`);
  if (!response.ok) {
    throw new Error('Failed to load tasks');
  }
  const payload = await response.json();
  renderTasks(payload.items || []);
  return payload.items || [];
}

async function fetchStats() {
  const response = await fetch(`${API_BASE_URL}/tasks/stats`);
  if (!response.ok) {
    throw new Error('Failed to load stats');
  }
  const payload = await response.json();
  renderStats(payload);
  return payload;
}

function collectFormData(formElement) {
  const formData = new FormData(formElement);
  return {
    title: formData.get('title'),
    description: formData.get('description'),
    priority: formData.get('priority'),
    due_date: formData.get('due_date') || null,
  };
}

async function createTask(taskPayload) {
  const response = await fetch(`${API_BASE_URL}/tasks`, {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify(taskPayload),
  });

  if (!response.ok) {
    const payload = await response.json();
    throw new Error(payload.error || 'Unable to create task');
  }

  return response.json();
}

function bindForm() {
  if (typeof document === 'undefined') {
    return;
  }
  const form = document.getElementById('task-form');
  const message = document.getElementById('form-message');
  if (!form || !message) {
    return;
  }

  form.addEventListener('submit', async (event) => {
    event.preventDefault();
    message.textContent = '';

    try {
      const taskPayload = collectFormData(form);
      await createTask(taskPayload);
      form.reset();
      await fetchTasks();
      await fetchStats();
    } catch (error) {
      message.textContent = error.message;
    }
  });
}

async function bootstrap() {
  bindForm();
  try {
    await fetchTasks();
    await fetchStats();
  } catch (error) {
    if (typeof document !== 'undefined') {
      const message = document.getElementById('form-message');
      if (message) {
        message.textContent = error.message;
      }
    }
  }
}

if (typeof globalThis !== 'undefined' && globalThis.addEventListener) {
  globalThis.addEventListener('DOMContentLoaded', bootstrap);
}

if (typeof module !== 'undefined') {
  module.exports = {
    collectFormData,
    formatDate,
    isUrgentTask,
    renderTaskCard,
    taskStatusBadge,
  };
}
