import React from 'react';
import '../assets/ResponseDisplayComponent.css';  // Import the CSS file
import '../assets/BarChart.css';

// This component is responsible for displaying the data returned from the request.
function ResponseDisplayComponent({ message }) {
  console.log('Received message:', message.data);  // Log to check if 'message' has 'data'

  // Verify message is not null and that it contains data and notify user if it does
  if (!message || !message.data || !Array.isArray(message.data) || message.data.length === 0) {
    return <p>No data available</p>;
  }

    // Display returned data in a table to the user.
  return (
    <div className="response-container">
      <h3 className="response-header">Response Data:</h3>
      <table className="response-table">
        <thead>
          <tr>
            <th>Rank</th>
            <th>Title</th>
            <th>Release Start</th>
            <th>Runtime</th>
            <th>Score</th>
            <th>Budget</th>
            <th>Box Office</th>
            <th>Genre</th>
            <th>Rating</th>
          </tr>
        </thead>
        <tbody>
          {message.data.map((dataEntry, index) => (
            <tr key={index}>
              <td>{dataEntry.rank}</td>
              <td>{dataEntry.title}</td>
              <td>{dataEntry.release_date}</td>
              <td>{dataEntry.runtime}</td>
              <td>{dataEntry.score}</td>
              <td>{dataEntry.budget}</td>
              <td>{dataEntry.boxoffice}</td>
              <td>{dataEntry.genre}</td>
              <td>{dataEntry.rating}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}


export default ResponseDisplayComponent;