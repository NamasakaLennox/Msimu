const Login = () => {
    const handleLoginSubmit = (event) => {
	event.preventDefault();

	const data = new FormData(event.target);
	const value = data.get("username");
	console.log(value)
    }
    const form = document.querySelector('form');
    if (form) {
	form.addEventListener('submit', handleLoginSubmit)
    }
    return (
	<section>
	    <div className="login-container">
		<h2>Login</h2>
		<form action="/" method="POST"
		      name="login" id="login">
		    <div>
			<label htmlFor="username">Username</label>
			<input type="text" name="username" id="username"
			       placeholder="" />
		    </div>
		    <div>
			<label htmlFor="password">Password</label>
                        <input type="password" name="password" id="password"
			       placeholder="" />
		    </div>
		    <input value="Login" type="submit" />
		</form>
	    </div>
	</section>
    );
}

export default Login;
