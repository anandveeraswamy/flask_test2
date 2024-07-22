# app.py

from flask import Flask
from flask import render_template, request, redirect, url_for

app = Flask(__name__)

# Task list
tasks = []

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/tasks")
def task_list():
    return render_template("tasks.html", tasks=tasks)

@app.route("/add", methods=["GET", "POST"])
def add_task():
    if request.method == "POST":
        task = request.form.get("task")
        tasks.append(task)
        return redirect(url_for("task_list"))
    return render_template("add.html")

@app.route("/delete/<int:task_id>", methods=["POST"])
def delete_task(task_id):
    try:
        if 0 <= task_id < len(tasks):
            tasks.pop(task_id)
        else:
            raise IndexError("Invalid task_id")
    except Exception as e:
        print("An error occurred:", e)
    return redirect(url_for("task_list"))

if __name__ == "__main__":
    app.run(debug=True)
