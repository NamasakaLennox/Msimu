import "../styles/live.css";
import Loading from "./Loading";

import React, { useState, useEffect } from "react";
/* import './WeatherApp.css'; */

const LiveData = () => {
  const [weatherData, setWeatherData] = useState(null);
  const apiKey = "9b1bf9ad224448abb9462854230705";

  useEffect(() => {
    fetch(`https://api.weatherapi.com/v1/current.json?key=${apiKey}&q=Eldoret`)
      .then((response) => response.json())
      .then((data) => setWeatherData(data));
  }, []);

  if (!weatherData) {
    return (
      <div>
        <Loading />
      </div>
    );
  }

  return (
    <section>
      <div className="live-container">
        <div className="live-child live">
          <h4>
            {weatherData.location.name}, {weatherData.location.country}
          </h4>
          <div className="data">
            <img src={weatherData.current.condition.icon} alt="weather image" />
            <strong className="temp">{weatherData.current.temp_c}&deg;C</strong>
          </div>
          <p>
            Feels like {weatherData.current.feelslike_c}&deg;C.{" "}
            {weatherData.current.condition.text}
          </p>
          <div>
            <h4>Other Relevant Weather Information:</h4>
            <ul>
              <li>
                <strong>Wind:</strong> {weatherData.current.wind_kph}{" "}
                {weatherData.current.wind_dir}
              </li>
              <li>
                <strong>UV Index:</strong> {weatherData.current.uv}%
              </li>
              <li>
                <strong>Visibility:</strong> {weatherData.current.vis_km}km
              </li>
            </ul>
            <ul>
              <li>
                <strong>Atm. Pressure:</strong>{" "}
                {weatherData.current.pressure_mb} mb
              </li>
              <li>
                <strong>Humidity:</strong> {weatherData.current.humidity}%
              </li>
            </ul>
          </div>
        </div>
        <div class-name="live-child map">
          {/* <img
            src="https://www.meteoblue.com/en/weather/maps/basel_switzerland_2661604#coords=11.51/-1.315/36.8551&map=windAnimation~rainbow~auto~10%20m%20above%20gnd~none"
            alt="weather map"
            className="weathermap"
          /> */}
          <iframe
            src="https://tilecache.rainviewer.com/v2/radar/1701549000/256/1/1000/1000/3/0_0.png"
            className="weathermap"
          ></iframe>
        </div>
      </div>
    </section>
  );
};

export default LiveData;
