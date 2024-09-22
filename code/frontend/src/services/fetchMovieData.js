const fetchMovieData = async (input1, input2) => {
    const response = await fetch('http://localhost:5000/api/getData', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ input1, input2 }),
    });

    if (!response.ok) {
        throw new Error('Network response was not ok');
    }
    return await response.json();
};

export default fetchMovieData;
