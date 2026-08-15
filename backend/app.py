from flask import Flask, jsonify, request

app = Flask(__name__)

# Temporary task storage
tasks = []


@app.route("/")
def home():
    return jsonify({
        "message": "AI Task Management Backend is running!"
    })


@app.route("/api/health")
def health():
    return jsonify({
        "status": "healthy"
    })


# Get all tasks
@app.route("/api/tasks", methods=["GET"])
def get_tasks():
    return jsonify({
        "tasks": tasks
    })


# Create a new task
@app.route("/api/tasks", methods=["POST"])
def create_task():
    data = request.get_json()

    task = {
        "id": len(tasks) + 1,
        "title": data.get("title"),
        "description": data.get("description"),
        "status": "pending"
    }

    tasks.append(task)

    return jsonify({
        "message": "Task created successfully",
        "task": task
    }), 201

# Update a task
@app.route("/api/tasks/<int:task_id>", methods=["PUT"])

def update_task(task_id):
    data = request.get_json()

    for task in tasks:
        if task["id"] == task_id:
            task["title"] = data.get("title", task["title"])
            task["description"] = data.get(
                "description",
                task["description"]
            )
            task["status"] = data.get("status", task["status"])

            return jsonify({
                "message": "Task updated successfully",
                "task": task
            })

    return jsonify({
        "error": "Task not found"
    }), 404


if __name__ == "__main__":
    app.run(debug=True)