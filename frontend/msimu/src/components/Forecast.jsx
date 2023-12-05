import "../styles/forecast.css";
import React, { useState, useEffect } from "react";
import Loading from "./Loading";

const Weather = ({
  labels,
  avgTempCData,
  dailyChanceOfRainData,
  totalPrecipMmData,
  imgLinks,
}) => {
  return (
    <div className="cards-container">
      {labels.map((label, index) => (
        <div className="card" key={index}>
          <img src={imgLinks[index]} alt="weather image description" />
          <h4>{label}</h4>
          <ul>
            <li>Rainfall chances: {dailyChanceOfRainData[index]}%</li>
            <li>Rainfall amount: {totalPrecipMmData[index]}mm</li>
            <li>Avg. Temp: {avgTempCData[index]}&deg;C</li>
          </ul>
        </div>
      ))}
    </div>
  );
};

export default function Forecast() {
  const [weatherData, setWeatherData] = useState(null);

  const apiKey = "9b1bf9ad224448abb9462854230705";

  useEffect(() => {
    fetch(
      `https://api.weatherapi.com/v1/forecast.json?key=${apiKey}&q=Barcelona&days=6&aqi=no`
    )
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

  const avgTempCData = [];

  const dailyChanceOfRainData = [];

  const totalPrecipMmData = [];

  const imgLinks = [];

  const months = ["Nov", "Dec", "Jan", "Feb", "Mar", "Apr"];

  weatherData.forecast.forecastday.forEach((day) => {
    avgTempCData.push(day.day.avgtemp_c);

    dailyChanceOfRainData.push(day.day.totalprecip_mm);

    totalPrecipMmData.push(day.day.daily_chance_of_rain);

    imgLinks.push(day.day.condition.icon);
  });
  return (
    <section>
      <div className="title">
        <h2>Forecast</h2>
      </div>
      {/* will duplicate the cards 5 times */}
      <Weather
        labels={months}
        avgTempCData={avgTempCData.concat(avgTempCData)}
        dailyChanceOfRainData={dailyChanceOfRainData.concat(
          dailyChanceOfRainData
        )}
        totalPrecipMmData={totalPrecipMmData.concat(totalPrecipMmData)}
        imgLinks={imgLinks.concat(imgLinks)}
      />
    </section>
  );
}
