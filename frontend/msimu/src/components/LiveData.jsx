import cloud from "../img/cloud.png"
import weathermap from "../img/weathermap.png"
import styles from "../styles/live.css"

export default function LiveData() {
    return (
	<section>
	    <div className="live-container">
		<div className="live-child live">
		    <h4>Eldoret, Ke</h4>
		    <div className="data">
			<img src={cloud} alt="weather image" />
			<strong className="temp">20&deg;C</strong>
		    </div>
		    <p>Feels like 20&deg;C. Scattered clouds. Gentle Breeze</p>
		    <div>
			<h4>Other Relevant Weather Information:</h4>
			<ul>
			    <li><strong>Wind:</strong> 4.6m/s SSW</li>
			    <li><strong>Dew point:</strong> 9&deg;C</li>
			    <li><strong>Visibility:</strong> 10.0km</li>
			</ul>
			<ul>
			    <li><strong>Atm. Pressure:</strong> 992hPa</li>
			    <li><strong>Humidity:</strong> 91%</li>
			</ul>
		    </div>
		</div>
		<div class-name="live-child map">
		    <img src={weathermap} alt="weather map"
			 className="weathermap"/>
		</div>
	    </div>
	</section>
    )
}
