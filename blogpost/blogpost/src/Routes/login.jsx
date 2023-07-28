import React, { useState, useEffect } from "react";
import { useNavigate } from "react-router-dom";
import "./loginCSS.css";

const Login = () => {
  const navigate = useNavigate();
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [users, setUsers] = useState([]);

  const handleSubmit = () => {
    fetch("http://127.0.0.1:8000/")
      .then((response) => response.json())
      .then((json) => setUsers(json))
      .catch((error) => console.log("error", error));

    users.map((user) => {
      if (email === user.email && password === user.password) {
        navigate(`/blogs/${user.uid}`);
      }
    });
  };

  useEffect(() => {
    handleSubmit();
  }, []);

  return (
    <div className="container">
      <h1>Blog Post</h1>
      <div className="login">
        <form onSubmit={handleSubmit}>
          <table>
            <tr>
              <td>
                <input
                  type="email"
                  value={email}
                  onChange={(e) => setEmail(e.target.value)}
                  placeholder="Enter Email"
                />
              </td>
            </tr>
            <tr>
              <td>
                <input
                  type="password"
                  value={password}
                  onChange={(e) => setPassword(e.target.value)}
                  placeholder="Enter password"
                />
              </td>
            </tr>
            <tr>
              <td>
                <input type="submit" value="Login" />
              </td>
            </tr>
          </table>
        </form>
      </div>
    </div>
  );
};

export default Login;
