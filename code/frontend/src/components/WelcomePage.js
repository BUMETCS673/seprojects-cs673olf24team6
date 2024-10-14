import React from 'react';
import { Link } from 'react-router-dom';
import '../assets/WelcomePage.css';

function WelcomePage() {
  return (
    <div className="welcome-page">
      <h1 className="header"><i> BLOCKBUSTER MOVIES </i></h1>
      <div>
        <center>
          <Link to="/submitform" className="button-link">GET STARTED!</Link>
        </center>
      </div>
    </div>
  );
}

export default WelcomePage;