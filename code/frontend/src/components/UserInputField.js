import React from 'react';
// User input feilds componenet that is a component we abstract to utilize in several palces across the system.
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