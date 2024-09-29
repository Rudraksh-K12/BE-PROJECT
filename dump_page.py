# dump_page.py

import streamlit as st
from streamlit_server_state import server_state

# This is the function for the dump/landing page
def dump_page():
    st.title("Welcome to the Dump Page!")
    st.write("You have successfully logged in.")

    if st.button("Logout"):
        server_state.logged_in = False  # Clear the login state
        server_state.login_time_server = None  # Clear the login time
        st.session_state.logged_in = False
        st.session_state.login_time = None  # Clear the session time
        st.experimental_rerun()  # Go back to login page after logging out
