import Logo from "../img/logo.png"
import "../styles/nav.css"

export default function Navbar() {
    return (
	<header className="header">
	    <a href="/">
		<img src={Logo} alt="logo" className="logo" />
	    </a>
	    <nav className="navbar">
		<ul id="header-list">
		    <li><a href="/">Home</a></li>
		    <li><a href="/about">About</a></li>
		    <li><a href="/community">Community</a></li>
		    <li><a href="/signup">Sign Up</a></li>
		    <li><a href="/login">Login</a></li>
		</ul>
	    </nav>
	</header>
    );
}