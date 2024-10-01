import React from 'react'
import '@testing-library/jest-dom';
import MovieQueryFormComponent from "../components/MovieQueryFormComponent";
import {render, act, waitFor} from "@testing-library/react";

//fetch mock function
global.fetch = jest.fn(() =>
    Promise.resolve({
        text: () => Promise.resolve('<form id="submitForm"></form>')
    })
);

describe('MovieQueryFormComponent', () => {
    const setData = jest.fn();
    const setLoading = jest.fn();

    const consoleErrorSpy = jest.spyOn(console, 'error').mockImplementation(() => {});

    beforeEach(() => {
        fetch.mockClear();
        setData.mockClear();
        setLoading.mockClear();
        document.body.innerHTML = '<div id="formContainer"></div>';
    });

    afterAll(() => {
        consoleErrorSpy.mockRestore();
    });


    test("Fetch the HTML file and insert it into the container", async () => {
        fetch.mockImplementationOnce(() =>
            Promise.resolve({
                text: () => Promise.resolve('<form id="submitForm"></form>') // Simulate form HTML
            })
        );

        await act(async () => {
            render(<MovieQueryFormComponent setData={setData} setLoading={setLoading} />);
        });

        //checks if the HTML form has been inserted into the container
        const formContainer = document.getElementById('formContainer');
        expect(formContainer.innerHTML).toContain('submitForm');
        expect(fetch).toHaveBeenCalledWith('/submitform.html');

    });

    test("handles failed to load html", async () => {
        fetch.mockImplementationOnce(() => Promise.reject("API failure"));
        await act(async () => {
            render(<MovieQueryFormComponent setData={setData} setLoading={setLoading} />);
        });
        const formContainer = document.getElementById('formContainer');

        await waitFor(() => {
            expect(consoleErrorSpy).toHaveBeenCalledWith('Failed to load HTML:', "API failure");
        });

    });
});
