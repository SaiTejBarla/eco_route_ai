import folium
from streamlit_folium import st_folium

def plot_route(route, origin, destination):
    """
    Display a folium map for a given route.
    route: single route dict (from get_route)
    origin, destination: "lon,lat" strings
    """
    o_lon, o_lat = map(float, origin.split(","))
    d_lon, d_lat = map(float, destination.split(","))

    # Center map on midpoint
    m = folium.Map(location=[(o_lat + d_lat) / 2, (o_lon + d_lon) / 2], zoom_start=13)

    # Markers
    folium.Marker([o_lat, o_lon], tooltip="Origin", icon=folium.Icon(color="green")).add_to(m)
    folium.Marker([d_lat, d_lon], tooltip="Destination", icon=folium.Icon(color="red")).add_to(m)

    # Route polyline
    if "geometry" in route:
        folium.GeoJson(route["geometry"], name="Route").add_to(m)

    # Return map object instead of rendering
    return m


def score_routes(distance_m, duration_s, co2_g):
    """Score routes: lower is better (weighted eco + time)."""
    return (0.5 * (distance_m / 1000)) + (0.3 * (duration_s / 60)) + (0.2 * (co2_g / 100))
