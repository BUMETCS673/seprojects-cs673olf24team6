import React from 'react';
import { render, fireEvent } from '@testing-library/react';
import { MemoryRouter, Routes, Route } from 'react-router-dom';
import userEvent from '@testing-library/user-event';
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

  test('renders the dropdown input; while also checking that it take a option', async () => {
    const { getByTestId } = render(
      <MemoryRouter>
        <MovieQueryFormPage />
      </MemoryRouter>
    );
    const user = userEvent.setup();

    const dropdownRating = getByTestId("rating");
    const dropdownGenre = getByTestId("genre");

    expect(dropdownRating).toBeInTheDocument();
    expect(dropdownGenre).toBeInTheDocument();

    await user.selectOptions(dropdownGenre, "Drama");
    await user.selectOptions(dropdownRating, "R");

    expect(dropdownGenre.value).toBe("1");
    expect(dropdownRating.value).toBe("1");
  });

  test('renders the clear button; Tests teh clear functionality', async () => {
    const { getByText, getByRole, getByTestId } = render(
      <MemoryRouter>
        <MovieQueryFormPage />
      </MemoryRouter>
    );
    const user = userEvent.setup();

    const buttonElement = getByText(/Clear/i);
    const inputElement = getByRole("spinbutton");
    const dropdownRating = getByTestId("rating");
    const dropdownGenre = getByTestId("genre");

    expect(buttonElement).toBeInTheDocument();
    expect(inputElement).toBeInTheDocument();
    expect(dropdownRating).toBeInTheDocument();
    expect(dropdownGenre).toBeInTheDocument();

    const value = 1990;

    fireEvent.change(inputElement, { target: { value } });
    await user.selectOptions(dropdownGenre, "Drama");
    await user.selectOptions(dropdownRating, "R");

    expect(inputElement.value).toBe("1990");
    expect(dropdownGenre.value).toBe("1");
    expect(dropdownRating.value).toBe("1");

    fireEvent.click(buttonElement);

    expect(inputElement.value).toBe("");
    expect(dropdownGenre.value).toBe("");
    expect(dropdownRating.value).toBe("");
  });
});
