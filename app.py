# app.py

import streamlit as st
from login_page import login_page
from dump_page import dump_page
from streamlit_server_state import server_state
from datetime import datetime, timedelta

def main():
    # Initialize the 'logged_in' state and login time if they do not exist
    if 'logged_in' not in st.session_state:
        st.session_state.logged_in = False
    if 'login_time' not in st.session_state:
        st.session_state.login_time = None
    if 'logged_in' not in server_state:
        server_state.logged_in = False
    if 'login_time_server' not in server_state:
        server_state.login_time_server = None

    # Check if the user is logged in and if the session is still valid
    if st.session_state.logged_in or server_state.logged_in:
        # Check if the session has expired (TTL of 2 minutes) for server_state
        if server_state.logged_in and server_state.login_time_server:
            if datetime.now() - server_state.login_time_server > timedelta(minutes=1):
                server_state.logged_in = False  # Log out if TTL exceeded
                st.warning("Session expired! Please log in again.")
                login_page()  # Redirect to login page
                return  # Exit the main function after redirecting

        dump_page()  # Go to the dump page if logged in
    else:
        login_page()  # Show the login page if not logged in

if __name__ == "__main__":
    main()
