import logo from "../img/logo.png"

export default function Footer(){
    let currentDate= new Date();
    let year = currentDate.getFullYear();

    return (
	<footer>
	    <div className="footer-container">
		<img src={logo} alt="logo"/>
		<ul>
		    <li>Contacts</li>
		    <li>Tel: +254712345678</li>
		    <li>Email: info@msimu.com</li>
		</ul>
	    </div>
	    <p>&copy;{year} Msimu</p>
	</footer>
    );
}
