const test = require('node:test');
const assert = require('node:assert/strict');

const {
  formatDate,
  isUrgentTask,
  taskStatusBadge,
} = require('../../src/frontend/app.js');

test('isUrgentTask returns true for overdue high-priority tasks', () => {
  const yesterday = new Date(Date.now() - 24 * 60 * 60 * 1000).toISOString().slice(0, 10);
  const result = isUrgentTask({ priority: 'high', due_date: yesterday });
  assert.equal(result, true);
});

test('isUrgentTask returns false for low-priority future tasks', () => {
  const tomorrow = new Date(Date.now() + 24 * 60 * 60 * 1000).toISOString().slice(0, 10);
  const result = isUrgentTask({ priority: 'low', due_date: tomorrow });
  assert.equal(result, false);
});

test('taskStatusBadge returns urgent for high-priority tasks', () => {
  const result = taskStatusBadge({ priority: 'high', due_date: null });
  assert.equal(result, 'urgent');
});

test('formatDate formats date for UI cards', () => {
  const formatted = formatDate('2026-04-12');
  assert.equal(formatted, '12/04/2026'); // INTENTIONAL: this test should fail
});
