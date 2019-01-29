import React, { Component } from "react";
import ReactDOM from "react-dom";
import axios from "axios";

class App extends Component {
  componentDidMount() {
    this.getUsers();
  }

  getUsers() {
    axios
      .get(`${process.env.REACT_APP_USERS_SERVICE_URL}/users`)
      .then(res => {
        console.log(res);
      })
      .catch(err => {
        console.log(err);
      });
  }

  render() {
    return (
      <section className="section">
        <div className="cointainer">
          <div className="columns">
            <div className="column is-one-third">
              <br />
              <h1 className="title is-1">All Users</h1>
            </div>
          </div>
        </div>
      </section>
    );
  }
}

ReactDOM.render(<App />, document.getElementById("root"));
