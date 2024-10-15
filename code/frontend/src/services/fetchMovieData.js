// src/services/fetchMovieData.js
export async function fetchMovieData(queryData) {
  try {
    const response = await fetch('http://localhost:5000/api/processQueryRequest', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify(queryData),
    });

    if (!response.ok) {
      throw new Error('Network response was not ok');
    }

    const result = await response.json();
    console.log('Server Response:', result);  // Check if 'result.data' is available
    return result;
  } catch (error) {
    console.error('Fetch error:', error);
    return { error: 'Unexpected response format' };  // Handle error case
  }
}

