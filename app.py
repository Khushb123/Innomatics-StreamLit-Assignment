import streamlit as st
import webbrowser

st.title("First Assignment Innomatics Research Labs")
st.header("Create Streamlit Data App")
st.subheader("Khushboo Singh")

linkedin = 'https://www.linkedin.com/in/khushboo-singh-94934a105'

if st.button('Linkedin'):
    webbrowser.open_new_tab(linkedin)

github = 'https://github.com/Khushb123'

if st.button('GitHub'):
    webbrowser.open_new_tab(github)