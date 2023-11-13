import React from 'react';
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import About from "./pages/About";
import Home from "./pages/Home";
import Login from "./pages/Login";
import Signup from "./pages/Signup";
import Navbar from "./components/Navbar";
import Footer from "./components/Footer";
import styles from "./styles/main.css";

export default function App() {
    return (
	    <Router>
		<Navbar />
		<Routes>
		    <Route path='/' element={<Home />}></Route>
		    <Route path='/about' element={<About />}></Route>
		    <Route path='/login' element={<Login />}></Route>
		    <Route path='/signup' element={<Signup />}></Route>
		</Routes>
		<Footer />
	    </Router>
    );
}
