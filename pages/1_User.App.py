import streamlit as st
from modules.data_fetch import get_route
from modules.routing import plot_route, score_routes
from modules.emissions import estimate_co2
from utils.helpers import format_seconds
from streamlit_folium import st_folium

st.title("🚗 EcoRoute AI - User Route Planner")
st.markdown("Plan your eco-friendly journey with real-time route optimization 🌱")

# Inputs
origin_lat = st.number_input("Origin Latitude", value=17.7386)
origin_lon = st.number_input("Origin Longitude", value=83.3167)
dest_lat = st.number_input("Destination Latitude", value=17.7196)
dest_lon = st.number_input("Destination Longitude", value=83.3030)

mode = st.selectbox("Mode", ["driving", "cycling", "walking"])

# Initialize session state
if "route_result" not in st.session_state:
    st.session_state.route_result = None
    st.session_state.origin = None
    st.session_state.destination = None

# When button clicked → fetch and save in session
if st.button("Get Route"):
    origin = f"{origin_lon},{origin_lat}"
    destination = f"{dest_lon},{dest_lat}"

    routes = get_route(origin, destination, profile=mode)

    if not routes:
        st.error("No routes found.")
    else:
        st.session_state.route_result = routes[0]   # Save best route
        st.session_state.origin = origin
        st.session_state.destination = destination

# --- Show results if we have a route ---
if st.session_state.route_result:
    route = st.session_state.route_result
    distance = route["distance"]
    duration = route["duration"]
    co2 = estimate_co2(distance, mode="car")
    score = score_routes(distance, duration, co2)

    st.success(
        f"**Distance:** {distance/1000:.2f} km | "
        f"**Duration:** {format_seconds(duration)} | "
        f"**CO₂:** {co2:.0f} g | "
        f"**Eco Score:** {score:.1f}"
    )

    # Show map
    m = plot_route(route, st.session_state.origin, st.session_state.destination)
    st_folium(m, width=700, height=500)
