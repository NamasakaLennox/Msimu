import cloud from "../img/cloud.png"

export default function Forecast() {
    return (
	<section>
	    <h2>Forecast</h2>
	    {/* will duplicate the cards 5 times */}
	    <div className="cards-container">
		<div className="card">
		    <img src={cloud} alt="weather image description" />
		    <h4>April</h4>
		    <ul>
			<li>Rainfall chances: 69%</li>
			<li>Rainfall amount: 2mm</li>
			<li>Avg. Temp: 29&deg;C</li>
		    </ul>
		</div>
		<div className="card">
		    <img src={cloud} alt="weather image description" />
		    <h4>May</h4>
		    <ul>
			<li>Rainfall chances: 69%</li>
			<li>Rainfall amount: 2mm</li>
			<li>Avg. Temp: 29&deg;C</li>
		    </ul>
		</div>
		<div className="card">
		    <img src={cloud} alt="weather image description" />
		    <h4>June</h4>
		    <ul>
			<li>Rainfall chances: 69%</li>
			<li>Rainfall amount: 2mm</li>
			<li>Avg. Temp: 29&deg;C</li>
		    </ul>
		</div>
		<div className="card">
		    <img src={cloud} alt="weather image description" />
		    <h4>July</h4>
		    <ul>
			<li>Rainfall chances: 69%</li>
			<li>Rainfall amount: 2mm</li>
			<li>Avg. Temp: 29&deg;C</li>
		    </ul>
		</div>
		<div className="card">
		    <img src={cloud} alt="weather image description" />
		    <h4>August</h4>
		    <ul>
			<li>Rainfall chances: 69%</li>
			<li>Rainfall amount: 2mm</li>
			<li>Avg. Temp: 29&deg;C</li>
		    </ul>
		</div>
		<div className="card">
		    <img src={cloud} alt="weather image description" />
		    <h4>September</h4>
		    <ul>
			<li>Rainfall chances: 69%</li>
			<li>Rainfall amount: 2mm</li>
			<li>Avg. Temp: 29&deg;C</li>
		    </ul>
		</div>
	    </div>
	</section>
    );
}
