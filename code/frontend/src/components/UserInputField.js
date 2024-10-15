import React from 'react';
// User input fields component that is a component we abstract to utilize in several places across the system.
function UserInputField({ label, name, type = 'text', value, onChange }) {
  return (
    <div className="input-field">
      <label htmlFor={name}>{label}:</label>
      <input
        id={name}
        name={name}
        type={type}
        value={value}
        onChange={onChange}
        className="input"
      />
    </div>
  );
}

export default UserInputField;