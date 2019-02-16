import React, { Component } from "react";
import axios from "axios";
import { Switch, Route } from "react-router-dom";
import UserList from "./components/UserList";
import AddUser from "./components/AddUser";
import About from "./components/About";
import Navbar from "./components/Navbar";
import Form from "./components/Form";
import Logout from "./components/Logout";
import UserStatus from "./components/UserStatus";

class App extends Component {
  constructor(props) {
    super(props);
    this.state = {
      users: [],
      title: "Testdriven.io",
      isAuthenticated: false
    };
    this.logoutUser = this.logoutUser.bind(this);
    this.loginUser = this.loginUser.bind(this);
  }

  componentDidMount() {
    this.getUsers();
  }

  componentWillMount() {
    if (window.localStorage.getItem("authToken")) {
      this.setState({ isAuthenticated: true });
    }
  }

  getUsers() {
    axios
      .get(`${process.env.REACT_APP_USERS_SERVICE_URL}/users`)
      .then(res => {
        this.setState({ users: res.data.data.users });
      })
      .catch(err => {
        console.log(err);
      });
  }

  logoutUser() {
    window.localStorage.clear();
    this.setState({ isAuthenticated: false });
  }

  loginUser(token) {
    window.localStorage.setItem("authToken", token);
    this.setState({ isAuthenticated: true });
    this.getUsers();
  }

  render() {
    return (
      <div>
        <Navbar
          title={this.state.title}
          isAuthenticated={this.state.isAuthenticated}
        />
        <section className="section">
          <div className="cointainer">
            <div className="columns">
              <div className="column is-half">
                <br />
                <Switch>
                  <Route
                    exact
                    path="/"
                    render={() => <UserList users={this.state.users} />}
                  />
                  <Route exact path="/about" component={About} />
                  <Route
                    exact
                    path="/register"
                    render={() => (
                      <Form
                        formType={"Register"}
                        formData={this.state.formData}
                        handleUserFormSubmit={this.handleUserFormSubmit}
                        handleFormChange={this.handleFormChange}
                        isAuthenticated={this.state.isAuthenticated}
                      />
                    )}
                  />
                  <Route
                    exact
                    path="/login"
                    render={() => (
                      <Form
                        formType={"Login"}
                        isAuthenticated={this.state.isAuthenticated}
                        loginUser={this.loginUser}
                      />
                    )}
                  />
                  <Route
                    exact
                    path="/logout"
                    render={() => (
                      <Logout
                        logoutUser={this.logoutUser}
                        isAuthenticated={this.state.isAuthenticated}
                      />
                    )}
                  />
                  <Route
                    exact
                    path="/status"
                    render={() => (
                      <UserStatus
                        isAuthenticated={this.state.isAuthenticated}
                      />
                    )}
                  />
                </Switch>
              </div>
            </div>
          </div>
        </section>
      </div>
    );
  }
}

export default App;
