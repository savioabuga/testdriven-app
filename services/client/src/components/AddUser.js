import React from "react";

const AddUser = () => {
  return (
    <form>
      <div className="field">
        <input
          name="username"
          type="text"
          className="input is-large"
          placeholder="Enter a username"
          required
        />
      </div>
      <div className="field">
        <input
          type="email"
          className="input is-large"
          name="email"
          placeholder="Enter an email address"
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
