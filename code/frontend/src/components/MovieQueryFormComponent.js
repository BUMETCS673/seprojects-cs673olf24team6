import React, { useState } from 'react';
import UserInputField from './UserInputField';
import { fetchMovieData } from '../services/fetchMovieData';
import '../assets/SubmitFormPage.css';


// This is the form that will hold the input fields and handle the call the function responsible for
// fetching data from backend
function MovieQueryFormComponent({ setData, setLoading }) {

  // Using number values for simplicity
  // Years allowed are between 1900 and current year
  const currentYear = new Date().getFullYear();
  const years = Array.from(new Array(100), (val, index) => currentYear - index);


  // Form and its data fields
  const [formData, setFormData] = useState({
    release_after: '',
    genre_select: '',
    rating_select: '',
  });

  // Capture and handle input changes
  const handleInputChange = (e) => {
    const { name, value } = e.target;
    setFormData({
      ...formData,
      [name]: value
    });
  };

  // Handle submission press
  const handleSubmit = async (e) => {
    e.preventDefault();  // Prevents page from reloading
    setLoading(true);

    try {
      const result = await fetchMovieData(formData);
      if (result && result.data) {
        console.log("MQF: ",  JSON.stringify(result.data, null, 2));
        setData(result);  // Set the response data
      } else {
        setData([]);  // If no data return, return empty array
        console.log('Received message: Unexpected response format');
      }
    } catch (error) {
      console.error('Fetch error:', error);
      setData([]);  // If no data return, return empty array
    } finally {
      setLoading(false);  // Show loading
    }
  };

  // Clear button functionality
  const handleClear = () => {
    setFormData({
    release_after: '',
    genre_select: '',
    rating_select: '',
  });
  };

// Input fields to be displayed to user.
return (
  <form id="submitForm" onSubmit={handleSubmit}>
    <div className="leftcol">

        <UserInputField
          label="Released After"
          name="release_after"
          type="number"  // This will need to a num
          value={formData.release_start}
          onChange={handleInputChange}
          min="1900"
          max={new Date().getFullYear()}
        />


      <div className="input">
        <label htmlFor="genre_select">Genres: </label>
        <select
          name="genre_select"
          id="genre_select"
          value={formData.genre_select}
          onChange={handleInputChange}
        >
          <option value="" disabled>Select a Genre</option>
          <option value={1}>Drama</option>
          <option value={2}>Crime</option>
          <option value={3}>Action</option>
          <option value={4}>Biography</option>
          <option value={5}>History</option>
          <option value={6}>Adventure</option>
          <option value={7}>Western</option>
          <option value={8}>Romance</option>
          <option value={9}>Sci-Fi</option>
          <option value={10}>Fantasy</option>
          <option value={11}>Mystery</option>
          <option value={12}>Family</option>
          <option value={13}>Thriller</option>
          <option value={14}>War</option>
          <option value={15}>Comedy</option>
          <option value={16}>Animation</option>
          <option value={17}>Music</option>
          <option value={18}>Horror</option>
          <option value={19}>Film-Noir</option>
          <option value={20}>Musical</option>
          <option value={21}>Sport</option>
        </select>
      </div>


      <div className="input">
        <label htmlFor="rating_select">Rating: </label>
        <select
          name="rating_select"
          id="rating_select"
          value={formData.rating_select}
          onChange={handleInputChange}
        >
          <option value="" disabled>Select a Rating</option>
          <option value="1">R</option>
          <option value="2">PG-13</option>
          <option value="3">Approved</option>
          <option value="4">PG</option>
          <option value="5">18+</option>
          <option value="6">Not Rated</option>
          <option value="7">G</option>
          <option value="8">Passed</option>
          <option value="9">Not Available</option>
          <option value="10">TV-PG</option>
          <option value="11">Unrated</option>
          <option value="12">X</option>
          <option value="13">13+</option>
          <option value="14">TV-MA</option>
          <option value="15">GP</option>
          <option value="NC-17">NC-17</option>
        </select>
      </div>
    </div>

    {/* Buttons */}
    <button type="submit">Submit</button>  {/* This triggers the form's onSubmit handler */}
    <button type="button" onClick={handleClear}>Clear</button>  {/* This clears the form */}
  </form>
);

}

export default MovieQueryFormComponent;
