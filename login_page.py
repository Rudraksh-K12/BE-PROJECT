# login_app.py

import streamlit as st
from streamlit_server_state import server_state
from datetime import datetime

# Function to display the login page
def login_page():
    st.title("Login Page")

    # Create username and password input fields
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    remember_me = st.checkbox("Remember Me")

    # Hardcoded login credentials
    correct_username = "admin"
    correct_password = "hello@123"

    # Login validation
    if st.button("Login"):
        if username == correct_username and password == correct_password:
            if remember_me:
                server_state.logged_in = True  # Set server_state.logged_in to True if "Remember Me" is checked
                server_state.login_time_server = datetime.now()  # Store login time for server state
            st.session_state.logged_in = True  # Maintain login state for the session
            st.session_state.login_time = datetime.now()  # Store login time for session state
            st.success("Login successful!")
            st.experimental_rerun()  # Reload the app to go to the landing page
        else:
            st.error("Invalid username or password.")
