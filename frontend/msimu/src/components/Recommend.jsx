import graph from "../img/graph.png"

export default function Recommend() {
    return (
	<section>
	    <h2>Graphical Representation</h2>
	    <div className="graph-container">
		<div className="graph">
		    <img src={graph} alt="graphical representation" />
		</div>
		<div className="recommend-text">
		    <p>You should consider harvesting your crops soon to prevent drought-related losses.</p>
		</div>
	    </div>
	</section>
    );
}
