import React, { useEffect } from 'react';
import fetchMovieData from '../services/fetchMovieData';  // Import your data-fetching utility function


//This may need to be better refactor into more appropriate function calls so they may be unit tested
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

        const data_request = {
            // Get input values from the dynamically loaded form
            rank : document.getElementById('rank').value,
            title : document.getElementById('title').value,
            release_start : document.getElementById('release_start').value,
            release_end : document.getElementById('release_end').value,
            score : document.getElementById('score').value,
            genre_select : document.getElementById('genre_select').value,
            rating_select : document.getElementById('rating_select').value,
            budget : document.getElementById('budget').value,
            box_office : document.getElementById('box_office').value,
            cast_select : document.getElementById('cast_select').value,
            director_select : document.getElementById('director_select').value,
            writer_select : document.getElementById('writer_select').value,
        };

        setLoading(true);  // Set loading state to true
        try {
            const result = await fetchMovieData(data_request);  // Fetch data using inputs
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