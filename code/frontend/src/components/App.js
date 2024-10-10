import React from 'react';
import { BrowserRouter as Router, Route, Routes, Link } from 'react-router-dom';
import WelcomePage from './WelcomePage';  // Import WelcomePage component
import SubmitFormPage from './SubmitFormPage';  // Import SubmitFormPage component

function App() {
  return (
    <Router>
      <div className="App">
        <Routes> {/* Routes are how React handles page navigation */}
          {/* Welcome Page Route */}
          <Route path="/" element={<WelcomePage />} />

          {/* Submit Form Page Route */}
          <Route path="/submitform" element={<SubmitFormPage />} />
        </Routes>
      </div>
    </Router>
  );
}

export default App;