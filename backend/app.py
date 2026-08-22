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


if __name__ == "__main__":
    app.run(debug=True)