const Signup = () => {
    const handleSignupSubmit = (event) => {
        event.preventDefault();

        const data = new FormData(event.target);
        const value = data.get("username");
        console.log(value)
    }
    const form = document.querySelector('form');
    if (form) {
        form.addEventListener('submit', handleSignupSubmit)
    }
    return (
        <section>
            <div className="signup-container">
                <h2>Sign Up</h2>
                <form action="/" method="POST"
                      name="signup" id="signup">
		    <div>
                        <label htmlFor="first_name">First Name</label>
                        <input type="text" name="first_name" id="first_name"
                               placeholder="John" />
                    </div>
		    <div>
                        <label htmlFor="last_name">Last Name</label>
                        <input type="text" name="last_name" id="last_name"
                               placeholder="Doe" />
                    </div>
                    <div>
                        <label htmlFor="username">Username</label>
                        <input type="text" name="username" id="username"
                               placeholder="johndoe" />
                    </div>
		    <div>
                        <label htmlFor="phone">Phone Number</label>
                        <input type="text" name="phone" id="phone"
                               placeholder="+254712345678" />
                    </div>
		    <div>
                        <label htmlFor="email">Email</label>
                        <input type="text" name="email" id="email"
                               placeholder="johndoe@example.com" />
                    </div>
                    <div>
                        <label htmlFor="password">Password</label>
                        <input type="password" name="password" id="password"
                               placeholder="" />
                    </div>
		    <div>
                        <label htmlFor="password_c">Confirm Password</label>
                        <input type="password" name="password_c" id="password_c"
                               placeholder="" />
                    </div>
                    <input value="Sign Up" type="submit" />
                </form>
            </div>
        </section>
    );
}

export default Signup;
