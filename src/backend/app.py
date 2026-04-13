from flask import Flask, jsonify, request
from flask_cors import CORS

from task_service import create_task, filter_tasks_by_priority, get_task, list_tasks, task_stats
from task_utils import validate_priority

app = Flask(__name__)
CORS(app)


@app.get("/health")
def health_check():
    return jsonify({"status": "ok"})


@app.get("/tasks")
def get_tasks():
    priority = request.args.get("priority")
    tasks = filter_tasks_by_priority(priority) if priority else list_tasks()
    return jsonify({"items": tasks, "count": len(tasks)})


@app.get("/tasks/<task_id>")
def get_task_by_id(task_id):
    task = get_task(task_id)
    if task is None:
        return jsonify({"error": "Task not found"}), 404
    return jsonify(task)


@app.post("/tasks")
def post_task():
    payload = request.get_json(silent=True) or {}

    title = str(payload.get("title", "")).strip()
    if not title:
        return jsonify({"error": "Field 'title' is required"}), 400

    priority = str(payload.get("priority", "medium")).strip().lower()
    if not validate_priority(priority):
        return jsonify({"error": "Field 'priority' must be high, medium or low"}), 400

    task = create_task(
        title=title,
        description=payload.get("description", ""),
        priority=priority,
        due_date=payload.get("due_date"),
    )
    return jsonify(task), 201


@app.get("/tasks/stats")
def get_stats():
    return jsonify(task_stats())


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=False)
