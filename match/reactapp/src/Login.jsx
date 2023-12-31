import React, { useState, useEffect } from "react";
import axios from "axios";
import ashesicampus from "./components/icons/ashesicampus.jpg";
import ashesilogo from "./components/icons/ashesilogo.png";
import { useNavigate, Routes, Route } from "react-router-dom";
import HomePage from "./HomePage"; // Import HomePage
import Cookies from "js-cookie";

const ProtectedHome = ({ token }) => {
  const navigate = useNavigate();

  return <HomePage/>; // Render HomePage if authorized
};

const Login = (props) => {
  const [email, setEmail] = useState("");
  const [pass, setPass] = useState("");
  const navigate = useNavigate();

  // Move useEffect inside Login component
  useEffect(() => {
    setupAxiosInterceptors();
  }, []);

  function setupAxiosInterceptors() {
    axios.interceptors.request.use((config) => {
      const token = Cookies.get("token");
      if (token) {
        config.headers.Authorization = `token ${token}`;
      }
      return config;
    });
  }

  const handleSubmit = async (e) => {
    e.preventDefault();

    try {
      const response = await axios.post(
        "http://127.0.0.1:8000/accounts/login/",
        {
          email,
          password: pass,
        }
      );
      // Extract token from response data
      Cookies.set("token", response.data.token, { secure: true, httpOnly: true });
      navigate("/");
    } catch (error) {
      console.error("Error:", error.message);
      // Implement proper error handling here
    }
  };

  return (
    <Routes>
      <Route
        path="/"
        element={
          <div style={{
            position: "relative",
            display: "flex",
            justifyContent: "center",
            alignItems: "center",
            height: "100vh",
          }}>
            <img src={ashesicampus} alt="Ashesi Campus" style={{ width: "100%" }} />
            <div className="auth-form-container" style={{
              position: "absolute",
              padding: "20px",
              width: "400px",
              background: "rgba(255, 255, 255, 0.636)",
              borderRadius: "10px",
              textAlign: "center",
            }}>
              <div style={{ display: "flex", flexDirection: "column", alignItems: "center" }}>
                <img src={ashesilogo} alt="Ashesi Logo" style={{
                  width: "50%",
                  margin: "20px",
                }} />
                <h4 style={{ marginBottom: "30px", textAlign: "left" }}>Login</h4>
              </div>
              <form className="login-form" onSubmit={handleSubmit} style={{
                display: "flex",
                flexDirection: "column",
                alignItems: "left",
              }}>
                <label htmlFor="email" style={{ textAlign: "left" }}>
                  Email
                </label>
                <input value={email} onChange={(e) => setEmail(e.target.value)} type="email" id="email" name="email" style={{
                  marginBottom: "10px",
                }} />
                <label htmlFor="password" style={{ textAlign: "left" }}>
                  Password
                </label>
                <input value={pass} onChange={(e) => setPass(e.target.value)} type="password" id="password" name="password" style={{
                  marginBottom: "10px",
                }} />

                <button type="submit" onClick={handleSubmit} style={{
                  marginTop: "20px",
                  width: "30%",
                  color: "white",
                  background: "#AD3537",
                  borderRadius: "5px",
                  borderColor: "#AD3537",
                  marginLeft: "35%",
                }}>
                  Login
                </button>

              </form>
              <div className="link-btn" onClick={() => props.onFormSwitch("login")} style={{
                marginTop: "20px",
                marginBottom: "20px",
                textAlign: "center", // Centered the text
              }}>
                Don't have an account? Register here.
              </div>
            </div>
          </div>
        }
      />
      <Route path="/" element={<ProtectedHome navigate={navigate} token={Cookies.get("token")} />} />
    </Routes>
  );
};

export default Login;