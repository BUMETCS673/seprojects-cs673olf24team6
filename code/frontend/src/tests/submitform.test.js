import React from 'react'
import {render, screen, waitFor, fireEvent} from '@testing-library/react'
import userEvent from '@testing-library/user-event'

const fs = require('fs');
const path = require('path');
const html = fs.readFileSync(path.resolve('public/submitform.html'), 'utf8');


jest.dontMock('fs');

test("The Rank Input should not take a text", () => {
    render(
    <>
        <meta name="csrf-token" content="mocked-token" />
    </>);

    document.documentElement.innerHTML = html.toString();
    const input = document.getElementById("rank");
    const value = "test";

    fireEvent.change(input, {
            target: {
                value
            }
    });
    expect(input.value).toBe("");
})

test("the Rank Input should take a number", () => {
    render(
    <>
        <meta name="csrf-token" content="mocked-token" />
    </>);

    document.documentElement.innerHTML = html.toString();
    const input = document.getElementById("rank");
    const value = 1;

    fireEvent.change(input, {
            target: {
                value
            }
    });
    expect(input.value).toBe("1");
})

test("the Title input field should take a text input", async () => {
    render(
    <>
        <meta name="csrf-token" content="mocked-token" />
    </>);

    document.documentElement.innerHTML = html.toString();
    const input = document.getElementById("title");
    const value = "Movie";

    fireEvent.change(input, {
            target: {
                value
            }
    });
    expect(input.value).toBe("Movie");
})

test("the Start Date input field should take a date", () => {
    render(
    <>
        <meta name="csrf-token" content="mocked-token" />
    </>);

    document.documentElement.innerHTML = html.toString();
    const input = document.getElementById("release_start");
    fireEvent.change(input, { target: { value: '2024-09-29' } });

    expect(input.value).toBe('2024-09-29');
})

test("the Start Date input field should not take a text", () => {
    render(
    <>
        <meta name="csrf-token" content="mocked-token" />
    </>);

    document.documentElement.innerHTML = html.toString();
    const input = document.getElementById("release_start");
    fireEvent.change(input, { target: { value: 'test' } });

    expect(input.value).toBe('');
})

test("the End Date input field should take a date", () => {
    render(
    <>
        <meta name="csrf-token" content="mocked-token" />
    </>);

    document.documentElement.innerHTML = html.toString();
    const input = document.getElementById("release_end");
    fireEvent.change(input, { target: { value: '2024-09-29' } });

    expect(input.value).toBe('2024-09-29');
})

test("the End Date input field should not take a text", () => {
    render(
    <>
        <meta name="csrf-token" content="mocked-token" />
    </>);

    document.documentElement.innerHTML = html.toString();
    const input = document.getElementById("release_end");
    fireEvent.change(input, { target: { value: 'test' } });

    expect(input.value).toBe('');
})

test("the Score Input should take a number", () => {
    render(
    <>
        <meta name="csrf-token" content="mocked-token" />
    </>);

    document.documentElement.innerHTML = html.toString();
    const input = document.getElementById("score");
    const value = 1;

    fireEvent.change(input, {
            target: {
                value
            }
    });
    expect(input.value).toBe("1");
})

test("The Score Input should not take a text", () => {
    render(
    <>
        <meta name="csrf-token" content="mocked-token" />
    </>);

    document.documentElement.innerHTML = html.toString();
    const input = document.getElementById("score");
    const value = "test";

    fireEvent.change(input, {
            target: {
                value
            }
    });
    expect(input.value).toBe("");
})

test("the Budget Input should take a number", () => {
    render(
    <>
        <meta name="csrf-token" content="mocked-token" />
    </>);

    document.documentElement.innerHTML = html.toString();
    const input = document.getElementById("budget");
    const value = 1;

    fireEvent.change(input, {
            target: {
                value
            }
    });
    expect(input.value).toBe("1");
})

test("The Budget Input should not take a text", () => {
    render(
    <>
        <meta name="csrf-token" content="mocked-token" />
    </>);

    document.documentElement.innerHTML = html.toString();
    const input = document.getElementById("budget");
    const value = "test";

    fireEvent.change(input, {
            target: {
                value
            }
    });
    expect(input.value).toBe("");
})

test("the Box Office Input should take a number", () => {
    render(
    <>
        <meta name="csrf-token" content="mocked-token" />
    </>);

    document.documentElement.innerHTML = html.toString();
    const input = document.getElementById("box_office");
    const value = 1;

    fireEvent.change(input, {
            target: {
                value
            }
    });
    expect(input.value).toBe("1");
})

test("The Box Office Input should not take a text", () => {
    render(
    <>
        <meta name="csrf-token" content="mocked-token" />
    </>);

    document.documentElement.innerHTML = html.toString();
    const input = document.getElementById("box_office");
    const value = "test";

    fireEvent.change(input, {
            target: {
                value
            }
    });
    expect(input.value).toBe("");
})