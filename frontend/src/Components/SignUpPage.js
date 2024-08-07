import React from "react";
import Header from "./Header";
import "../Styles/SignUpPage.css";
import { Link } from "react-router-dom";

export default function SignUpPage({ college }) {
  return (
    <>
      <Header isLoginPage>
        <Link to="/">
          <button className="nav-button">Back To Home</button>
        </Link>
      </Header>
      <div className="signup-page">
        <div className="signup-form">
          <h2>Register Account</h2>
          <form>
            {/* <div className="form-group input-group">
              <i className="fas fa-university"></i>
              <select required>
                <option value="">---Select your college---</option>
                {college.map((col) => (
                  <option key={col.id} value={col.id}>
                    {col.name}
                  </option>
                ))}
              </select>
            </div> */}
            <div className="form-group input-group">
              <i className="fas fa-id-card"></i>
              <input type="text" placeholder="Registration no..." required />
            </div>
            <div className="form-group input-group">
              <i className="fas fa-user"></i>
              <input type="text" placeholder="First name..." required />
            </div>
            <div className="form-group input-group">
              <i className="fas fa-user"></i>
              <input type="text" placeholder="Last name..." required />
            </div>
            <div className="form-group input-group">
              <i className="fas fa-envelope"></i>
              <input type="email" placeholder="Email..." required />
            </div>
            <div className="form-group input-group">
              <i className="fas fa-lock"></i>
              <input type="password" placeholder="Enter password..." required />
            </div>
            <div className="form-group input-group">
              <i className="fas fa-lock"></i>
              <input
                type="password"
                placeholder="Re-enter Password..."
                required
              />
            </div>
            <button type="submit">Register Account</button>
          </form>
          <p className="login-link">
            Already have an account?{" "}
            <Link to="/login">
              <span className="login-link-button">Login</span>
            </Link>
          </p>
        </div>
      </div>
    </>
  );
}
