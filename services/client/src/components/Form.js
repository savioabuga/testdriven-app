import React, { Component } from "react";
import { Redirect } from "react-router-dom";
import axios from "axios";

class Form extends Component {
  constructor(props) {
    super(props);
    this.state = {
      formData: {
        username: "",
        email: "",
        password: ""
      },
      valid: false
    };
    this.handleUserFormSubmit = this.handleUserFormSubmit.bind(this);
    this.handleFormChange = this.handleFormChange.bind(this);
  }
  componentDidMount() {
    this.clearForm();
  }
  componentWillReceiveProps(nextProps) {
    if (this.props.formType !== nextProps.formType) {
      this.clearForm();
    }
  }
  validateForm() {
    this.setState({ valid: true });
  }

  clearForm() {
    this.setState({
      formData: { username: "", email: "", password: "" }
    });
  }
  handleUserFormSubmit(e) {
    e.preventDefault();
    const formType = this.props.formType;
    const data = {
      email: this.state.formData.email,
      password: this.state.formData.password
    };

    if (formType === "Register") {
      data.username = this.state.formData.username;
    }

    const url = `${
      process.env.REACT_APP_USERS_SERVICE_URL
    }/auth/${formType.toLowerCase()}`;
    axios
      .post(url, data)
      .then(res => {
        this.clearForm();
        this.props.loginUser(res.data.auth_token);
      })
      .catch(err => {
        console.log(err);
      });
  }

  handleFormChange(e) {
    const obj = this.state.formData;
    obj[e.target.name] = e.target.value;
    this.setState(obj);
    // this.validateForm();
  }
  render() {
    if (this.props.isAuthenticated) {
      return <Redirect to="/" />;
    }
    return (
      <div>
        {this.props.formType === "Login" && (
          <h1 className="title is-1">Login</h1>
        )}
        {this.props.formType === "Register" && (
          <h1 className="title is-1">Register</h1>
        )}
        <hr />
        <br />
        <form onSubmit={e => this.handleUserFormSubmit(e)}>
          {this.props.formType === "Register" && (
            <div className="field">
              <input
                type="text"
                name="username"
                placeholder="Enter a username"
                className="input is-medium"
                required
                value={this.state.formData.username}
                onChange={this.handleFormChange}
              />
            </div>
          )}
          <div className="field">
            <input
              type="email"
              name="email"
              className="input is-medium"
              placeholder="Enter an email address"
              value={this.state.formData.email}
              onChange={this.handleFormChange}
            />
          </div>
          <div className="field">
            <input
              type="password"
              name="password"
              className="input is-medium"
              placeholder="Password"
              value={this.state.formData.password}
              onChange={this.handleFormChange}
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
  }
}

export default Form;
