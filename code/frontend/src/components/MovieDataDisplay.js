import React from 'react';

function MovieDataDisplay({ loading, data }) {
    return (
        <div>
            {loading ? <p>Loading...</p> : <p>{data}</p>}
        </div>
    );
}

export default MovieDataDisplay;
