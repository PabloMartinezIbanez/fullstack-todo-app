import { test, mock } from 'node:test';
import assert from 'node:assert';
import { collectFormData, formatDate, isUrgentTask, renderTaskCard, taskStatusBadge } from '../src/frontend/app.js';

test('isUrgentTask returns true for overdue high-priority tasks', () => {
  const task = { priority: 'high', due_date: '2023-01-01' };
  assert.strictEqual(isUrgentTask(task), true);
});

test('isUrgentTask returns false for low-priority future tasks', () => {
  const task = { priority: 'low', due_date: '2099-01-01' };
  assert.strictEqual(isUrgentTask(task), false);
});

test('taskStatusBadge returns urgent for high-priority tasks', () => {
  const task = { priority: 'high', due_date: '2023-01-01' };
  assert.strictEqual(taskStatusBadge(task), 'urgent');
});

test('formatDate formats date for UI cards', () => {
  const date = '2026-04-12';
  assert.strictEqual(formatDate(date), '12/04/2026');
});
