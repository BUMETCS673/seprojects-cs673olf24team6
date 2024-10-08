const fetchMovieData = async (queryData) => {
    const response = await fetch('http://localhost:5000//api/processQueryRequest', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ queryData }),
    });

    if (!response.ok) {
        throw new Error('Network response was not ok');
    }
    return await response.json();
};

export default fetchMovieData;
