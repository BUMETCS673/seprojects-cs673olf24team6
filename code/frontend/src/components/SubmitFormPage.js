import React, { useState, useEffect  } from 'react';
import MovieQueryFormComponent from './MovieQueryFormComponent';
import ResponseDisplayComponent from './ResponseDisplayComponent';

function SubmitFormPage() {
    // Allows us to store the response as n object to use
  const [responseMessage, setResponseMessage] = useState(null);
  // Manages the loading state after a query has been submitted
  const [loading, setLoading] = useState(false);

  // Log message to verify that response is being updated
  useEffect(() => {
    console.log('Response message in SubmitFormPage:', responseMessage);
  }, [responseMessage]);

  useEffect(() => {
    console.log('Loading state:', loading);
  }, [loading]);

  return (
      <div>
        <h2>Submit Your Movie Query</h2>

        {/* Pass setData to handle response from the form submission */}
        <MovieQueryFormComponent setData={setResponseMessage} setLoading={setLoading} />

        {loading && <p>Loading...</p>}

        {!loading && responseMessage && <ResponseDisplayComponent message={responseMessage} />}

        {!loading && !responseMessage && <p>No data available yet.</p>}
      </div>
    );
}

export default SubmitFormPage;
