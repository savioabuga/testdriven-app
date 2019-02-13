import React from "react";

const Form = props => {
  return (
    <div>
      {props.formType === "Login" && <h1 className="title is-1">Login</h1>}
      {props.formType === "Register" && (
        <h1 className="title is-1">Register</h1>
      )}
      <hr />
      <br />
      <form onSubmit={e => props.handleUserFormSubmit(e)}>
        {props.formType === "Register" && (
          <div className="field">
            <input
              type="text"
              name="username"
              placeholder="Enter a username"
              required
              value={props.formData.username}
              onChange={props.handleFormChange}
            />
          </div>
        )}
        <div className="field">
          <input
            type="email"
            name="email"
            className="input is-medium"
            placeholder="Enter an email address"
            value={props.formData.email}
            onChange={props.handleFormChange}
          />
        </div>
        <div className="field">
          <input
            type="password"
            name="password"
            className="input is-medium"
            placeholder="Enter an email address"
            value={props.formData.password}
            onChange={props.handleFormChange}
          />
        </div>
        <input
          type="submit"
          value="Submit"
          className="button is-primary is-medium is-fullwidth"
        />
      </form>
    </div>
  );
};

export default Form;
