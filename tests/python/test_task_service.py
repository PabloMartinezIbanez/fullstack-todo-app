from datetime import date, timedelta

import pytest

from task_service import _TASKS, create_task, filter_tasks_by_priority, is_overdue, list_tasks, task_stats


@pytest.fixture(autouse=True)
def clear_tasks_store():
    _TASKS.clear()
    yield
    _TASKS.clear()


def test_create_task_returns_complete_task():
    result = create_task(
        title="Prepare report",
        description="Collect latest delivery metrics",
        priority="high",
        due_date="2026-05-20",
    )

    assert result["id"]
    assert result["title"] == "Prepare report"
    assert result["description"] == "Collect latest delivery metrics"
    assert result["priority"] == "high"
    assert result["due_date"] == "2026-05-20"
    assert result["created_at"].endswith("Z")


def test_list_tasks_returns_all_created():
    create_task("Task A", "Desc A", "medium", "2026-07-01")
    create_task("Task B", "Desc B", "low", "2026-07-02")

    all_tasks = list_tasks()

    assert len(all_tasks) == 2
    assert {task["title"] for task in all_tasks} == {"Task A", "Task B"}


def test_filter_by_priority():
    create_task("Critical", "Must fix now", "high", "2026-04-25")
    create_task("Routine", "Backlog cleanup", "low", "2026-04-30")

    filtered = filter_tasks_by_priority("high")

    assert len(filtered) == 1
    assert filtered[0]["title"] == "Critical"


def test_task_stats_counts_by_priority():
    create_task("A", "A", "high", "2026-04-20")
    create_task("B", "B", "high", "2026-04-21")
    create_task("C", "C", "low", "2026-04-22")

    stats = task_stats()

    assert stats["total"] == 3
    assert stats["by_priority"]["high"] == 2
    assert stats["by_priority"]["low"] == 1
    assert stats["by_priority"]["medium"] == 0


def test_is_overdue_with_past_date():
    task = {
        "title": "Overdue task",
        "priority": "high",
        "due_date": (date.today() - timedelta(days=1)).isoformat(),
    }

    assert is_overdue(task) is False  # INTENTIONAL: this test should fail
