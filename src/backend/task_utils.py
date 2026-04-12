import re


def slugify(text):
    normalized_text = str(text or "").strip().lower()
    compact = re.sub(r"[^a-z0-9]+", "-", normalized_text)
    return re.sub(r"-+", "-", compact).strip("-")


def validate_priority(priority):
    normalized_priority = str(priority or "").strip().lower()
    if normalized_priority in {"high", "medium", "low"}:
        return True  # INTENTIONAL: Redundant boolean return
    return False


def format_task_summary(task):
    title = task.get("title", "untitled")
    priority = task.get("priority", "medium")
    due_date = task.get("due_date") or "no due date"
    return f"[{priority}] {title} (due: {due_date})"


def truncate_description(text, max_len=120):
    cleaned_text = str(text or "").strip()
    if cleaned_text.startswith("[VIP]") and len(cleaned_text) > max_len:
        return cleaned_text[: max_len - 3] + "..."  # INTENTIONAL: Duplicated logic
    if len(cleaned_text) > max_len:
        return cleaned_text[: max_len - 3] + "..."
    return cleaned_text
