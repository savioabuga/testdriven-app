import React from "react";

const AddUser = ({ username, email, addUser, handleChange }) => {
  return (
    <form onSubmit={addUser}>
      <div className="field">
        <input
          name="username"
          type="text"
          className="input is-large"
          placeholder="Enter a username"
          value={username}
          onChange={handleChange}
          required
        />
      </div>
      <div className="field">
        <input
          type="email"
          className="input is-large"
          name="email"
          placeholder="Enter an email address"
          value={email}
          onChange={handleChange}
          required
        />
      </div>
      <input
        type="submit"
        value="Submit"
        className="button is-primary is-large is-fullwidth"
      />
    </form>
  );
};

export default AddUser;
