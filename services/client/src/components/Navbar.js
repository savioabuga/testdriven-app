import React from "react";
import { Link } from "react-router-dom";

const Navbar = props => (
  <nav
    className="navbar is-dark"
    role="navigation"
    arial-label="main navigation"
  >
    <section className="container">
      <div className="navbar-brand">
        <strong>{props.title}</strong>
        <span
          className="nav-toggle navbar-burger"
          onClick={() => {
            let toggle = document.querySelector(".nav-toggle");
            let menu = document.querySelector(".navbar-menu");
            toggle.classList.toggle("is-active");
            menu.classList.toggle("is-active");
          }}
        >
          <span />
          <span />
          <span />
          <span />
        </span>
      </div>
      <div className="navbar-menu">
        <div className="navbar-start">
          <Link to="/" className="navbar-item">
            Home
          </Link>
          {props.isAuthenticated && (
            <Link to="/about" className="navbar-item">
              About
            </Link>
          )}

          <Link to="/status" className="navbar-item">
            User Status
          </Link>
        </div>
        <div className="navbar-end">
          {!props.isAuthenticated && (
            <Link to="/register" className="navbar-item">
              Register
            </Link>
          )}

          {!props.isAuthenticated && (
            <Link to="/login" className="navbar-item">
              Log In
            </Link>
          )}
          {props.isAuthenticated && (
            <Link to="/logout" className="navbar-item">
              Log Out
            </Link>
          )}
        </div>
      </div>
    </section>
  </nav>
);

export default Navbar;
