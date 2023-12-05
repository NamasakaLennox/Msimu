import "../styles/footer.css";
import React from "react";

export default function Footer() {
  let currentDate = new Date();
  let year = currentDate.getFullYear();

  return (
    <footer className="footer">
      <div className="footer__addr">
        <h1 className="footer__logo">Msimu</h1>
        <h2>Contact</h2>
        <address>
          Tel: +254712345678
          <br />
          <a className="footer__btn" href="mailto:info@msimu.com">
            Email Us
          </a>
        </address>
      </div>
      <ul className="footer__nav">
        <li className="nav__item">
          <h2 className="nav__title">Social</h2>
          <ul className="nav__ul">
            <li>
              <a href="#">Twitter</a>
            </li>

            <li>
              <a href="#">Instagram</a>
            </li>
            <li>
              <a href="#">Reddit</a>
            </li>
          </ul>
        </li>

        <li className="nav__item">
          <h2 className="nav__title">Pages</h2>
          <ul className="nav__ul">
            <li>
              <a href="/about">About</a>
            </li>
            <li>
              <a href="http://localhost:3000/" target="_blank">
                Community
              </a>
            </li>
            <li>
              <a href="#">Home</a>
            </li>
          </ul>
        </li>
      </ul>
      <div className="legal">
        <p>&copy;{year} Msimu. All rights reserved.</p>
      </div>
    </footer>
  );
}
