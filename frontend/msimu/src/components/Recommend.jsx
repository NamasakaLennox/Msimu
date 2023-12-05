import "../styles/recommend.css";
import React, { useState, useEffect } from "react";
import { Chart, registerables } from "chart.js";
import { Line } from "react-chartjs-2";
import Loading from "./Loading";
Chart.register(...registerables);

const prediction = {'26': 0.0, '27': 0.08543276, '28': 0.27826658, '29': 0.2015045, '30': 0.05066111, '01': 0.286184, '02': 0.11073771, '03': 0.10567841, '04': 0.11846804, '05': 0.05445268, '06': 0.14263698, '07': 0.17369744, '08': 0.22405852, '09': 0.26414666, '10': 0.18870555, '11': 0.22116697, '12': 0.18725386, '13': 0.14674246, '14': 0.20087792, '15': 0.03101675, '16': 0.2089536, '17': 0.043828603, '18': 0.18277143, '19': 0.10230653, '20': 0.22713168, '21': 0.0023124237, '22': 0.28774795, '23': 0.0, '24': 0.0, '25': 0.03124115}

const rainfall = Object.values(prediction)

const labels = Object.keys(prediction)

export default function Recommend() {
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

  const rainFallData = [];

  const temperatureData = [];

  weatherData.forecast.forecastday.forEach((day) => {
    rainFallData.push(day.day.totalprecip_mm);
    temperatureData.push(day.day.avgtemp_c);
  });

  console.log(rainFallData, temperatureData);
  const data = {
    labels: labels,
    datasets: [
      {
        label: "Predicted Rainfall",
        data: rainfall,
        fill: false,
        backgroundColor: "rgba(75,192,192,0.2)",
        borderColor: "rgba(75,192,192,1)",
      },
    ],
  };
  return (
    <section>
      <div className="title">
        <h2>Graphical Representation</h2>
      </div>
      <div className="graph-container">
        <div className="graph">
          <h4>1 Month Rainfall Prediction Chart</h4>
          <div className="chart-container">
            <Line data={data} className="chart" />
          </div>
        </div>
        <div className="recommend-text">
          <h4>Recommendation to Farmer</h4>
          <p>
            You should consider harvesting your crops soon to prevent
            drought-related losses.
          </p>
          <p></p>
        </div>
      </div>
    </section>
  );
}
