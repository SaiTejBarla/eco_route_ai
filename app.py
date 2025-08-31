import streamlit as st
from pathlib import Path

# Page setup
st.set_page_config(
    page_title="EcoRoute AI",
    page_icon="🌱",
    layout="wide",
    initial_sidebar_state="expanded",
)

# App Title
st.title("🌱 EcoRoute AI — Smart & Green Routing for Visakhapatnam")

# Description
st.markdown(
    """
    Welcome to **EcoRoute AI** 🚀.  
    Optimize your commute and reduce your carbon footprint.  

    **Use the sidebar to navigate:**
    - 🧑‍🤝‍🧑 **User App** → Plan eco-friendly commutes.  
    - 🏙️ **City Planner** → Analyze traffic & emissions data.  
    """
)

# Logo (safe check)
logo_path = Path("assets/logo.png")
if logo_path.exists() and logo_path.stat().st_size > 0:
    st.image(str(logo_path), width=120)
else:
    st.warning("⚠️ Logo not found. Please add `assets/logo.png`.")
