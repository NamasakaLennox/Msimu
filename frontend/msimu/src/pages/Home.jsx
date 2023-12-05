import LiveData from "../components/LiveData";
import Forecast from "../components/Forecast";
import Recommend from "../components/Recommend";
import React from "react";
import Welcome from "../components/Welcome";

export default function Home() {
  return (
    <>
      <Welcome />
      <LiveData />
      <Forecast />
      <Recommend />
    </>
  );
}
