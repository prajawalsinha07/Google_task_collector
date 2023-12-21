from flask import Flask, jsonify, request
import sqlite3

app = Flask(__name__)

def get_db_connection():
    conn = sqlite3.connect('tasks.db')
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/api/tasks', methods=['GET'])
def get_tasks():
    try:
        conn = get_db_connection()
        tasks = conn.execute('SELECT * FROM Tasks').fetchall()
        conn.close()
        return jsonify([dict(task) for task in tasks])
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/api/tasks', methods=['POST'])
def create_task():
    try:
        new_task = request.json
        conn = get_db_connection()
        conn.execute('INSERT INTO Tasks (taskSource, taskDescription, taskState, timeAcquired, timeCompleted) VALUES (?, ?, ?, ?, ?)',
                     (new_task['taskSource'], new_task['taskDescription'], new_task['taskState'], new_task['timeAcquired'], new_task['timeCompleted']))
        conn.commit()
        conn.close()
        return jsonify(new_task), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
