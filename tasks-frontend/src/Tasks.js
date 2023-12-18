import React, { useState, useEffect } from 'react';

function Tasks() {
  const [tasks, setTasks] = useState([]);

  useEffect(() => {
    fetch('http://localhost:3000/') //Adjust URL based on Flask server
      .then(response => response.json())
      .then(data => setTasks(data));
  }, []);

  return (
    <div>
      <h1>Tasks</h1>
      <ul>
        {tasks.map(task => (
          <li key={task.title}>
            <h2>{task.title}</h2>
            <p>{task.content}</p>
            <p>Due: {task.due}</p>
            <p>Status: {task.status}</p>
          </li>
        ))}
      </ul>
    </div>
  );
}

export default Tasks;
