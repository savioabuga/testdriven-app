import React from "react";
import { Redirect } from "react-router-dom";

const Form = props => {
  if (props.isAuthenticated) {
    return <Redirect to="/" />;
  }

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
              className="input is-medium"
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
            placeholder="Password"
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
