import React, { Component } from "react";
import axios from "axios";
import { Switch, Route } from "react-router-dom";
import UserList from "./components/UserList";
import AddUser from "./components/AddUser";
import About from "./components/About";
import Navbar from "./components/Navbar";
import Form from "./components/Form";

class App extends Component {
  constructor(props) {
    super(props);
    this.handleChange = this.handleChange.bind(this);
    this.addUser = this.addUser.bind(this);
  }

  state = {
    users: [],
    username: "",
    email: "",
    title: "Testdriven.io",
    formData: {
      username: "",
      email: "",
      password: ""
    }
  };

  componentDidMount() {
    this.getUsers();
  }

  addUser(e) {
    e.preventDefault();

    const data = {
      username: this.state.username,
      email: this.state.email
    };

    axios
      .post(`${process.env.REACT_APP_USERS_SERVICE_URL}/users`, data)
      .then(res => {
        this.getUsers();
        this.setState({ username: "", email: "" });
      })
      .catch(err => console.log(err));
  }

  handleChange(e) {
    const obj = {};
    obj[e.target.name] = e.target.value;
    this.setState(obj);
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

  render() {
    return (
      <div>
        <Navbar title={this.state.title} />
        <section className="section">
          <div className="cointainer">
            <div className="columns">
              <div className="column is-half">
                <br />
                <Switch>
                  <Route
                    exact
                    path="/"
                    render={() => (
                      <div>
                        <h1 className="title is-1">All Users</h1>
                        <hr />
                        <br />
                        <AddUser
                          username={this.state.username}
                          email={this.state.email}
                          addUser={this.addUser}
                          handleChange={this.handleChange}
                        />
                        <br />
                        <br />
                        <UserList users={this.state.users} />
                      </div>
                    )}
                  />
                  <Route exact path="/about" component={About} />
                  <Route
                    exact
                    path="/register"
                    render={() => (
                      <Form
                        formType={"Register"}
                        formData={this.state.formData}
                      />
                    )}
                  />
                  <Route
                    exact
                    path="/login"
                    render={() => (
                      <Form formType={"Login"} formData={this.state.formData} />
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
