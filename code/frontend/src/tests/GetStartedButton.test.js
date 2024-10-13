import React from 'react';
import { render, fireEvent } from '@testing-library/react';
import { MemoryRouter, Routes, Route } from 'react-router-dom';
import WelcomePage from '../components/WelcomePage';
import SubmitFormPage from '../components/SubmitFormPage';  // Import the SubmitFormPage component
import MovieQueryFormPage from '../components/MovieQueryFormComponent';  // Import the SubmitFormPage component

describe('WelcomePage Component', () => {
  test('renders the GET STARTED! button with correct text and class', () => {
    const { getByText } = render(
      <MemoryRouter>
        <WelcomePage />
      </MemoryRouter>
    );

    const buttonElement = getByText(/get started!/i);
    expect(buttonElement).toBeInTheDocument();
    expect(buttonElement).toHaveClass('button-link');
  });

  test('navigates to the /submitform route when the button is clicked', () => {
    const { getByText } = render(
      <MemoryRouter initialEntries={['/']}>  // Set initial route to root
        <Routes>
          <Route path="/" element={<WelcomePage />} />
          <Route path="/submitform" element={<SubmitFormPage />} />  {/* Mock the submit page */}
        </Routes>
      </MemoryRouter>
    );

    const buttonElement = getByText(/get started!/i);
    fireEvent.click(buttonElement);  // Simulate button click

    // Now check if it navigated to /submitform
    expect(getByText(/Submit Your Movie Query/i)).toBeInTheDocument();  // Verify navigation by checking if the new page content is rendered
  });
});

describe('MovieQueryFormPage Component', () => {
  test('renders the release input; while also checking that it take a number', () => {
    const { getByRole } = render(
      <MemoryRouter>
        <MovieQueryFormPage />
      </MemoryRouter>
    );

    const inputElement = getByRole("spinbutton");
    expect(inputElement).toBeInTheDocument();
    const value = 1990;

    fireEvent.change(inputElement, { target: { value } });
    expect(inputElement.value).toBe("1990");
  });
});
