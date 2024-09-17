import React, { useEffect } from 'react';
import fetchMovieData from '../services/fetchMovieData';  // Import your data-fetching utility function


//This may need to be better refactor into more approiate fuinction calls so they may be unit tested
function MovieQueryFormComponent({ setData, setLoading }) {
    useEffect(() => {
        // Fetch the HTML file and insert it into the container
        fetch('/submitform.html')
            .then(response => response.text())  // Convert response to text (HTML)
            .then(html => {
                // Inject the fetched HTML into the div with id 'formContainer'
                document.getElementById('formContainer').innerHTML = html;

                // Attach event listener to the dynamically loaded form
                const form = document.getElementById('submitForm');
                form.addEventListener('submit', handleSubmit);
            })
            .catch(err => console.error('Failed to load HTML:', err));
    }, []);

    // Handle form submission
    const handleSubmit = async (e) => {
        e.preventDefault();  // Prevent default form submission behavior

        // Get input values from the dynamically loaded form
        const input1 = document.getElementById('input1').value;
        const input2 = document.getElementById('input2').value;

        setLoading(true);  // Set loading state to true
        try {
            const result = await fetchMovieData(input1, input2);  // Fetch data using inputs
            setData(result.message);  // Set the data received from the backend
        } catch (error) {
            setData('Error retrieving data');
        } finally {
            setLoading(false);  // Set loading state to false
        }
    };

    // This return a template html file not an inline html file
    return (
        // Container where the HTML form will be dynamically injected
        <div id="formContainer"></div>
    );
}

export default MovieQueryFormComponent;