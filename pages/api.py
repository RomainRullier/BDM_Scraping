import streamlit as st

st.title("API")

st.components.v1.iframe("http://localhost:8000/docs", width=800, height=1200)