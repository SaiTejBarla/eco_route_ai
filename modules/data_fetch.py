import requests

OSRM_URL = "http://router.project-osrm.org/route/v1"

def get_route(origin, destination, profile="driving"):
    """
    Fetch a route from OSRM demo server.
    origin, destination: "lon,lat" strings
    profile: driving | cycling | walking
    """
    try:
        url = f"{OSRM_URL}/{profile}/{origin};{destination}?overview=full&geometries=geojson"
        r = requests.get(url)
        if r.status_code != 200:
            return []
        data = r.json()
        routes = []
        for route in data.get("routes", []):
            routes.append({
                "distance": route["distance"],   # meters
                "duration": route["duration"],   # seconds
                "geometry": route["geometry"],   # geojson line
            })
        return routes
    except Exception as e:
        print("OSRM error:", e)
        return []


def get_weather(api_key, city="Visakhapatnam"):
    """Fetch current weather using OpenWeather API."""
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    try:
        return requests.get(url).json()
    except:
        return {}
