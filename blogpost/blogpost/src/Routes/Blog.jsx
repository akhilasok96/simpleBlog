import React, { useEffect, useState } from "react";
import { useParams } from "react-router-dom";
import "./blog_style.css";

function Blog() {
  const { id } = useParams();
  const [blogs, setBlogs] = useState([]);

  const apiBlog = () => {
    fetch(`http://127.0.0.1:8000/getBlog/${id}`)
      .then((response) => response.json())
      .then((json) => setBlogs(json))
      .catch((error) => console.log("error", error));
  };

  useEffect(() => {
    apiBlog();
  }, []);

  return (
    <div className="blogpage">
      <h1>Blog Page</h1>
      <form>
        <input type="submit" value="Add Post" />
      </form>
      <div className="blogcards">
        {blogs.map((blog) => {
          return (
            <div className="contents">
              <div className="title">
                <h3>{blog.ptitle}</h3>
              </div>
              <hr />
              <p id="text-content">{blog.pcontent}</p>
              <h5 id="blog-time">{blog.ptime}</h5>
            </div>
          );
        })}
      </div>
    </div>
  );
}

export default Blog;
