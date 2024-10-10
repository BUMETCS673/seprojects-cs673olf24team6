import React from 'react';

{/* Function is used to handle Loading and idle states when a query is submited */}
function MovieDataDisplay({ loading, data }) {
  // Handle loading state
  if (loading) {
    return <div>Loading...</div>;
  }

  // Handle no data state
  if (!data) {
    return <div>No data available</div>;
  }

  // Handle data display: format JSON data as string if it's an object or array
  // This is called a turney
  // Where is the data equals object type it will return the json, else it will return the data.
  const renderData = typeof data === 'object' ? JSON.stringify(data, null, 2) : data;

  {/* Preform data display for returned data */}
  return (
    <div>
      <h3>Movie Data</h3>
      <pre>{renderData}</pre>
    </div>
  );
}

export default MovieDataDisplay;
