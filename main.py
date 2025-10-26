import streamlit as st
import db_functions as db
from Scripts import app

# --- Page Configuration ---
st.set_page_config(
    page_title="Customer Segmentation Login",
    page_icon="👤",
    layout="centered"
)

# --- NEW: Functions for Login and Signup Pages ---

def login_page():
    """Displays the login page."""
    st.title("👤 Customer Segmentation Platform")
    st.write("Please log in to continue")

    with st.form("login_form"):
        st.subheader("Login")
        login_username = st.text_input("Username", key="login_user")
        login_password = st.text_input("Password", type="password", key="login_pass")
        login_button = st.form_submit_button("Log In")

        if login_button:
            if db.check_credentials(login_username, login_password):
                st.session_state["logged_in"] = True
                st.session_state["username"] = login_username
                st.success("Logged in successfully!")
                st.rerun()
            else:
                st.error("Invalid username or password.")
    
    # Button to switch to the signup page
    st.write("---")
    if st.button("Don't have an account? Sign Up"):
        st.session_state["page"] = "signup"
        st.rerun()

def signup_page():
    """Displays the signup page."""
    st.title("👤 Create a New Account")

    with st.form("signup_form"):
        st.subheader("Create an Account")
        signup_username = st.text_input("Choose a Username", key="signup_user")
        signup_password = st.text_input("Choose a Password", type="password", key="signup_pass")
        # ADDED: Confirm Password field
        signup_confirm_password = st.text_input("Confirm Password", type="password", key="signup_confirm_pass")
        
        signup_button = st.form_submit_button("Sign Up")

        if signup_button:
            # ADDED: Password confirmation logic
            if signup_password != signup_confirm_password:
                st.error("Passwords do not match. Please try again.")
            elif not signup_username or not signup_password:
                st.warning("Please enter a username and password.")
            elif db.user_exists(signup_username):
                st.warning("Username already exists. Please choose another.")
            else:
                db.add_user(signup_username, signup_password)
                st.success("Account created! You can now log in.")
                # Switch back to the login page after successful signup
                st.session_state["page"] = "login" 
                st.rerun()

    # Button to switch back to the login page
    st.write("---")
    if st.button("Already have an account? Log In"):
        st.session_state["page"] = "login"
        st.rerun()

# --- Main App Execution ---

# Initialize session state variables if they don't exist
if "logged_in" not in st.session_state:
    st.session_state["logged_in"] = False
if "page" not in st.session_state:
    st.session_state["page"] = "login" # Default to login page

# Main logic to display pages
if st.session_state["logged_in"]:
    # Display a logout button in the sidebar
    st.sidebar.success(f"Logged in as {st.session_state['username']}")
    if st.sidebar.button("Log Out"):
        # Clear session state on logout
        for key in st.session_state.keys():
            del st.session_state[key]
        st.rerun()
    
    # Run your main application
    app.run_app()
else:
    # Show signup page if the state is 'signup', otherwise show login
    if st.session_state["page"] == "signup":
        signup_page()
    else:
        login_page()