import React, { useState, useEffect } from 'react';

function Tasks() {
  const [tasks, setTasks] = useState([]);

  useEffect(() => {
    // Fetch tasks from the Flask API
    fetch('http://localhost:5000/api/tasks')
      .then(response => response.json())
      .then(data => setTasks(data))
      .catch(error => {
        // Handle any errors here
        console.error('Error fetching tasks:', error);
      });
  }, []);

  return (
    <div>
      <h1>Tasks</h1>
      <ul>
        {tasks.map(task => (
          <li key={task.taskID}>
            {task.taskDescription} (State: {task.taskState})
          </li> 
        ))}
      </ul>
    </div>
  );
}

export default Tasks;
