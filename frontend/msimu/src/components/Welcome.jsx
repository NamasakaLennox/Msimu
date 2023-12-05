import React from "react";
import "../styles/welcome.css";

const Welcome = () => {
  return (
    <div id="app" className="welcome">
      <article>
        <div className="container container_solid">
          <div className="title_wrapper">
            <h1>🌾 Welcome to Msimu! 🌿</h1>
          </div>
        </div>

        <div className="container container_image" aria-hidden="true">
          <div className="title_wrapper">
            <h1>🌾 Welcome to Msimu! 🌿</h1>
          </div>
        </div>
      </article>

      <section>
        <p>
          With Msimu, you're not just cultivating crops; you're cultivating
          success. Harness the power of data-driven decisions to optimize your
          yields, streamline operations, and nurture your agricultural dreams.{" "}
          <br></br>
          🌦️ Seize the Seasons:<br></br> Whether it's planting, harvesting, or
          preparing for the rainy season, Msimu ensures you're prepared for
          every agricultural endeavor. Let's grow together, harvest together,
          and thrive together.
        </p>
        <p>
          👩‍🌾 For Every Farmer, Everywhere:<br></br> Msimu is designed with you
          in mind. From small-scale farmers to agribusiness leaders, our
          platform adapts to your needs, ensuring a personalized and seamless
          farming experience. <br></br>
        </p>
      </section>
    </div>
  );
};
export default Welcome;
