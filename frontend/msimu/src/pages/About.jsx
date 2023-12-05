import React from "react";
import plantation from "../img/plantation.jpg";
import harvest from "../img/harvest.jpg";
import green from "../img/green.jpg";
import "../styles/about.css";

const About = () => {
  return (
    <section>
      <article>
        <div className="title">
          <h2>About Us</h2>
        </div>
        <div className="about-container">
          {/* add image for all sections */}
          <img src={plantation} alt="plantation" />
          <p style={{ padding: "10px", marginLeft: "20px" }}>
            Welcome to Msimu, where innovation meets agriculture. At Msimu, we
            are passionate about transforming the future of farming through
            cutting-edge technology. Our team of experts is committed to
            providing farmers with intuitive tools that harness the power of
            machine learning and real-time weather data.<br></br>
            <br></br> Whether you're a seasoned farmer or just starting, Msimu
            is your partner in cultivating success. Join us on this journey to
            revolutionize agriculture and usher in a new era of sustainable and
            efficient farming practices
          </p>
        </div>
      </article>
      <article>
        <div className="title">
          <h3>Our Mission</h3>
        </div>
        <div className="about-container">
          <p style={{ padding: "10px", marginLeft: "20px" }}>
            Our mission is to revolutionize agriculture through the seamless
            integration of technology. By leveraging advanced machine learning
            models and real-time weather data, we aim to empower farmers with
            actionable insights for informed decision-making. We are dedicated
            to enhancing crop management, optimizing planting and harvesting
            activities, and fostering a resilient agricultural community.{" "}
            <br></br>
            <br></br>
            Our vision is to be a driving force in creating sustainable,
            tech-enabled solutions that elevate the productivity and well-being
            of farmers worldwide
          </p>
          <img src={harvest} alt="harvest" />
        </div>
      </article>

      {/* <article>
        <div className="title">
          <h3>Inspiration</h3>
        </div>
        <div>
          <p></p>
        </div>
      </article> */}

      <article>
        <div className="title">
          <h3>Services</h3>
        </div>
        <div className="about-container">
          <img src={green} alt="green" />
          <p style={{ padding: "10px", marginLeft: "20px" }}>
            Msimu offers a comprehensive suite of services designed to
            revolutionize the agricultural experience. Our platform provides
            real-time weather data and precise rainfall predictions through
            advanced machine learning models. Farmers can effortlessly access
            personalized insights for optimal decision-making, from crop
            planting to harvesting. <br></br>
            <br></br>Whether you're seeking the latest weather updates or
            strategic recommendations for your farm activities, Msimu is your
            trusted companion in cultivating success. Join our digital
            agri-revolution and harness the power of data-driven farming for a
            sustainable and prosperous future.
          </p>
        </div>
      </article>

      {/* <article>
        <div className="title">
          <h3>Meet The Team</h3>
        </div>
        <div>
          <p></p>
        </div>
      </article> */}
    </section>
  );
};

export default About;
