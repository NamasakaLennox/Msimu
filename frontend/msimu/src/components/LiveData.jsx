import cloud from "../img/cloud.png"
import weathermap from "../img/weathermap.png"
import styles from "../styles/live.css"

export default function LiveData() {
    return (
	<section className="livedata">
	    <div>
		<h4>Eldoret, Ke</h4>
		<div>
		    <img src={cloud} alt="weather image" />
		    <strong>20&deg;C</strong>
		</div>
		<p>Feels like 20&deg;C. Scattered clouds. Gentle Breeze</p>
		<div>
		    <ul>
			<li>wind: 4.6m/s SSW</li>
			<li>Dew point:9&deg;C</li>
			<li>Visibility:10.0km</li>
		    </ul>
		    <ul>
			<li>Atm. Presuure: 992hPa</li>
			<li>Humidity:91%</li>
		    </ul>
		</div>
	    </div>
	    <div>
		<img src={weathermap} alt="weather map" />
	    </div>
	</section>
    )
}
