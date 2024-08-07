import React from "react";
import Header from "./Header";
import "../Styles/LoginPage.css";
// import { useEffect, useState } from "react";
// import axios from "axios";
import { Link } from "react-router-dom";

export default function LoginPage({ onLogInPageClosing, onSignUpPageOpening }) {
  // const[logindata,setlogindata]=useState([]);
  // useEffect(()=>{
  // axios.get("")

  // },[])
  function handleSubmit() {}
  return (
    <>
      <Header onLogInPageOpening={onLogInPageClosing} isLoginPage>
        <Link to="/">
          <button className="nav-button">Back To Home</button>
        </Link>
      </Header>
      <div className="login-page">
        <div className="login-form">
          <h2>Login</h2>
          <form>
            <div className="input-group">
              <i className="fas fa-envelope"></i>
              <input type="email" placeholder="Email" required />
            </div>
            <div className="input-group">
              <i className="fas fa-lock"></i>
              <input type="password" placeholder="Password" required />
            </div>
            <button type="submit" onClick={handleSubmit}>
              Login
            </button>
          </form>
          <p className="register-link">
            <span className="register-link-button">Forgot Password?</span>
          </p>
          <p className="register-link">
            Don't have an account?{" "}
            <Link to="/signup">
              <span
                className="register-link-button"
                onClick={onSignUpPageOpening}
              >
                Register
              </span>
            </Link>
          </p>
        </div>
      </div>
    </>
  );
}
