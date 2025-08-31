def estimate_co2(distance_m, mode="car"):
    """
    Rough CO₂ estimation.
    distance_m: meters
    mode: car | cycling | walking
    """
    if mode == "car":
        # Avg 120 g/km
        return (distance_m / 1000) * 120
    elif mode == "cycling":
        return (distance_m / 1000) * 5   # small food-energy impact
    elif mode == "walking":
        return (distance_m / 1000) * 2
    return 0
