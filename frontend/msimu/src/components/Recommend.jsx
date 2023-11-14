import graph from "../img/graph.png"
import styles from "../styles/recommend.css"

export default function Recommend() {
    return (
	<section>
	    <div className="title">
		<h2>Graphical Representation</h2>
	    </div>
	    <div className="graph-container">
		<div className="graph">
		    <h4>Rainfall Prediction Chart</h4>
		    <img src={graph} alt="graphical representation"
			 className="graph-img" />
		</div>
		<div className="recommend-text">
		    <h4>Recommendation to Farmer</h4>
		    <p>You should consider harvesting your crops soon to prevent drought-related losses.</p>
		    <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.</p>
		</div>
	    </div>
	</section>
    );
}
