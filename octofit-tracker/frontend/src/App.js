import React, { useEffect, useState } from 'react';
import { BrowserRouter as Router, Route, Routes, Link } from 'react-router-dom';
import './App.css';

function App() {
  const [users, setUsers] = useState([]);
  const [activities, setActivities] = useState([]);

  useEffect(() => {
    fetch('http://localhost:8000/api/users/')
      .then(response => response.json())
      .then(data => {
        console.log('Users API response:', data);
        setUsers(data);
      })
      .catch(error => console.error('Error fetching users:', error));

    fetch('http://localhost:8000/api/activities/')
      .then(response => response.json())
      .then(data => {
        console.log('Activities API response:', data);
        setActivities(data);
      })
      .catch(error => console.error('Error fetching activities:', error));
  }, []);

  return (
    <Router>
      <div className="container">
        <nav className="navbar navbar-expand-lg navbar-light bg-light">
          <div className="container-fluid">
            <Link className="navbar-brand" to="/">OctoFit Tracker</Link>
          </div>
        </nav>
        <div className="mt-4">
          <h1>Welcome to OctoFit Tracker</h1>
          <h2>Users</h2>
          <ul>
            {users.map(user => (
              <li key={user.id}>{user.name} - {user.email}</li>
            ))}
          </ul>
          <h2>Activities</h2>
          <ul>
            {activities.map(activity => (
              <li key={activity.id}>{activity.activity_type} - {activity.duration} minutes</li>
            ))}
          </ul>
        </div>
      </div>
    </Router>
  );
}

export default App;
