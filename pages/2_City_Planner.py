import streamlit as st
import folium
from streamlit_folium import st_folium
import random

st.set_page_config(page_title="EcoRoute AI - City Planner", layout="wide")

st.title("🏙️ EcoRoute AI - City Planner Dashboard")
st.markdown("Analyze city-wide traffic & emissions for smarter planning 🌍")

# ------------------- Sidebar Filters -------------------
st.sidebar.header("Filters")

zone = st.sidebar.selectbox(
    "Select Zone", ["All", "North", "South", "East", "West"], key="zone"
)
time_period = st.sidebar.selectbox(
    "Time Period", ["Morning Peak", "Afternoon", "Evening Peak", "Night"], key="time"
)

# Button to refresh data
if st.sidebar.button("🔄 Refresh Data"):
    st.session_state["regen"] = True
else:
    st.session_state["regen"] = st.session_state.get("regen", False)

# ------------------- Define Zone Bounds -------------------
# Format: [lat_min, lat_max, lon_min, lon_max]
zone_bounds = {
    "North": [17.75, 17.78, 83.30, 83.34],
    "South": [17.70, 17.73, 83.30, 83.34],
    "East": [17.70, 17.78, 83.34, 83.37],
    "West": [17.70, 17.78, 83.27, 83.30],
    "All": [17.70, 17.78, 83.27, 83.37]
}

# ------------------- Generate Map and Points -------------------
if "city_map" not in st.session_state or st.session_state["regen"]:
    bounds = zone_bounds[zone]
    city_center = [17.7386, 83.3167]
    m = folium.Map(location=city_center, zoom_start=13)

    random.seed(42)  # deterministic for demo
    points = []

    # Simulate traffic points
    num_points = 30
    if time_period in ["Afternoon", "Night"]:
        num_points = 15  # less traffic off-peak

    for _ in range(num_points):
        lat = random.uniform(bounds[0], bounds[1])
        lon = random.uniform(bounds[2], bounds[3])
        congestion = random.choice(["Low", "Medium", "High"])
        points.append((lat, lon, congestion))

        # Add marker to map
        color = {"Low": "green", "Medium": "orange", "High": "red"}[congestion]
        folium.CircleMarker(
            location=[lat, lon],
            radius=6,
            popup=f"Traffic: {congestion}",
            color=color,
            fill=True,
            fill_color=color,
        ).add_to(m)

    # Save in session_state
    st.session_state["points"] = points
    st.session_state["city_map"] = m
    st.session_state["regen"] = False

# ------------------- City Overview Metrics -------------------
st.subheader("📊 City Overview")
col1, col2 = st.columns(2)
col1.metric("Average CO₂ Emissions", value=350, delta="g/km")
col2.metric("Average Speed", value=42, delta="km/h")

st.markdown("---")

# ------------------- Traffic Heatmap -------------------
st.subheader("🚦 Traffic Heatmap")
st_folium(st.session_state["city_map"], width=700, height=500)

st.info("This is demo data. Can be connected to live traffic & emissions APIs.")
