import React, { useState } from 'react';
import FormComponent from './MovieQueryFormComponent';
import MovieDataDisplay from './MovieDataDisplay';

function App() {
    const [data, setData] = useState('');
    const [loading, setLoading] = useState(false);

    return (

        // James or Alex Todo make this a template
        <div>
            {/* Render the form and pass setData and setLoading as props */}
            <FormComponent setData={setData} setLoading={setLoading} />
            {/* Render the data display component */}
            <MovieDataDisplay loading={loading} data={data} />
        </div>
    );
}

export default App;
