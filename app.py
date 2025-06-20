from flask import Flask, render_template, request, redirect

app = Flask(__name__)

tasks = []  # List to store tasks in memory

@app.route('/')
def index():
    return render_template("index.html", tasks=tasks)

@app.route('/add', methods=["POST"])
def add():
    task = request.form['task']
    tasks.append(task)  # Add task to the list
    return redirect('/')

@app.route('/delete/<int:id>')
def delete(id):
    if 0 <= id < len(tasks):
        tasks.pop(id)  # Remove task by index
    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)

