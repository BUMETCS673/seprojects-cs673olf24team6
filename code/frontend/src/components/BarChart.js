import React from 'react';
import { Bar } from 'react-chartjs-2';
import '../assets/BarChart.css'; // Importing the CSS file

const BarChart = () => {
    // Data and options for the bar chart
    const data = {
        labels: ['January', 'February', 'March', 'April', 'May', 'June'],
        datasets: [
            {
                label: 'Sales',
                data: [12, 19, 3, 5, 2, 3],
                backgroundColor: 'rgba(75, 192, 192, 0.6)',
                borderColor: 'rgba(75, 192, 192, 1)',
                borderWidth: 1,
            },
        ],
    };

    const options = {
        scales: {
            y: {
                beginAtZero: true,
            },
        },
    };

    return (
        <div className="chart-container">
            <h2>Top 5 Movies Based from Search</h2>
            <Bar data={data} options={options} />
        </div>
    );
};

export default BarChart;