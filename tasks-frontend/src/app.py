from flask import Flask, jsonify
import json

app = Flask(__name__)

# Function to load tasks data from a static JSON file
def load_tasks():
    with open('tasks.json', 'r') as file:
        return json.load(file)

# Route to serve tasks data
@app.route('/', methods=['GET'])
def get_tasks():
    tasks = load_tasks()
    print(tasks)
    return jsonify(tasks)

if __name__ == '__main__':
    app.run(debug=True)
