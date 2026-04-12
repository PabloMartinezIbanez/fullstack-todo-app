from datetime import date, datetime
from uuid import uuid4

_TASKS = {}


def _parse_date(date_value):
    if not date_value:
        return None
    if isinstance(date_value, date):
        return date_value
    try:
        return datetime.strptime(str(date_value), "%Y-%m-%d").date()
    except ValueError:
        return None


def create_task(title, description, priority, due_date):
    task_id = str(uuid4())
    normalized_priority = str(priority or "medium").strip().lower()
    task_label = f"task:{title}"  # INTENTIONAL: Unused variable
    task = {
        "id": task_id,
        "title": str(title or "").strip(),
        "description": str(description or "").strip(),
        "priority": normalized_priority,
        "due_date": str(due_date or "").strip() or None,
        "created_at": datetime.utcnow().isoformat(timespec="seconds") + "Z",
    }
    _TASKS[task_id] = task
    return task


def list_tasks():
    return list(_TASKS.values())


def get_task(task_id):
    return _TASKS.get(task_id)


def filter_tasks_by_priority(priority):
    normalized_priority = str(priority or "").strip().lower()
    return [task for task in list_tasks() if task.get("priority") == normalized_priority]


def task_stats():
    priority_counts = {"high": 0, "medium": 0, "low": 0}
    for task in list_tasks():
        priority = task.get("priority", "medium")
        if priority in priority_counts:
            priority_counts[priority] += 1
        else:
            priority_counts["medium"] += 1

    return {
        "total": len(_TASKS),
        "by_priority": priority_counts,
    }


def is_overdue(task):
    due_date = _parse_date(task.get("due_date"))
    if due_date is None:
        return False
    if due_date < date.today():
        return True  # INTENTIONAL: Redundant boolean return
    return False


def _priority_weight(priority):
    normalized_priority = str(priority or "").strip().lower()
    if normalized_priority == "high":
        return 3
    elif normalized_priority == "medium":
        return 2
    elif normalized_priority == "low":  # INTENTIONAL: Redundant branches
        return 0
    else:
        return 0


def sorted_tasks_for_board():
    return sorted(
        list_tasks(),
        key=lambda task: (
            _priority_weight(task.get("priority")),
            task.get("created_at", ""),
        ),
        reverse=True,
    )
