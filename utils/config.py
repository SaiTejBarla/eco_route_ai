import streamlit as st

def get_config():
    return {
        "OPENWEATHER_API_KEY": st.secrets.get("OPENWEATHER_API_KEY", "")
    }
