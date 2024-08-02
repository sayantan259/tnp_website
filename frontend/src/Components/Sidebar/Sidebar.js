import React from "react";
import { Link } from "react-router-dom";
import axios from "axios";
import apiClient from "../../services/api";

function Sidebar() {
  const logout = async (refreshToken) => {
    try {
      await apiClient.post("user/api/logout/", { refresh_token: refreshToken });
    } catch (error) {
      throw error.response.data;
    }
  };

  const handleLogout = async () => {
    const refreshToken = localStorage.getItem("refresh_token");
    try {
      await logout(refreshToken);
      localStorage.removeItem("access_token");
      localStorage.removeItem("refresh_token");

      // Remove the Authorization header
      axios.defaults.headers.common["Authorization"] = null;

      // Redirect to login page
      window.location.href = "/";
    } catch (error) {
      console.error("Logout failed:", error);
    }
  };

  return (
    <div className="app-sidebar">
      <Link to="/dashboard/companies" className="app-sidebar-link active">
        Companies
      </Link>
      <Link to="/dashboard/applied-companies" className="app-sidebar-link">
        Applied Companies
      </Link>
      <Link to="/dashboard/share-hr-contact" className="app-sidebar-link">
        Share HR Contact
      </Link>
      <Link to="/dashboard/share-company-contact" className="app-sidebar-link">
        Share Company Contact
      </Link>
      <Link to="/dashboard/hr-list" className="app-sidebar-link">
        HR List
      </Link>
      <Link to="/dashboard/my-hr-list" className="app-sidebar-link">
        My HR List
      </Link>
      <span className="app-sidebar-link" onClick={handleLogout}>
        Logout
      </span>
    </div>
  );
}

export default Sidebar;
