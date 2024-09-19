import React from 'react';
import ReactDOM from 'react-dom/client';
import './assets/index.css';
import App from './components/App';
// Renders the App component into the root element in the HTML file


const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(
  <React.StrictMode>
    <App />
  </React.StrictMode>
);