from flask import Flask, render_template, url_for, redirect, request
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///Tasks.db"
db.init_app(app)


class Tasks(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    taskName = db.Column(db.String(250), nullable=False)
    isDone = db.Column(db.Boolean, nullable=False)


@app.route("/")
def home():
    db.create_all()
    all_tasks = db.session.query(Tasks).all()
    return render_template("index.html", tasks=all_tasks)


@app.route("/add", methods=["POST", "GET"])
def add():
    if request.method == "POST":
        task_name = request.form["task_name"]
        done = False
        # with app.app_context():
        new_task = Tasks(taskName=task_name, isDone=done)
        db.session.add(new_task)
        db.session.commit()
        return redirect(url_for("home"))


@app.route("/checked")
def checked():
    id = request.args.get("task_id")
    task_selected = Tasks.query.get(id)
    task_selected.isDone = True
    db.session.commit()
    return redirect(url_for("home"))

@app.route("/delete")
def delete():
    id = request.args.get("task_id")
    task_selected = Tasks.query.get(id)
    db.session.delete(task_selected)
    db.session.commit()
    return redirect(url_for("home"))


if __name__ == "__main__":
    app.run(debug=True)
