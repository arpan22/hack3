import random

def fetch_aqi_data():
    """Mock AQI data for major US regions"""
    cities = [
        ("Los Angeles", 34.05, -118.25),
        ("New York", 40.71, -74.00),
        ("Chicago", 41.88, -87.63),
        ("Houston", 29.76, -95.36),
        ("Phoenix", 33.45, -112.07),
        ("Seattle", 47.61, -122.33),
        ("Denver", 39.74, -104.99),
        ("Miami", 25.76, -80.19),
        ("Dallas", 32.78, -96.80),
        ("Atlanta", 33.75, -84.39),
    ]

    data = []
    for name, lat, lon in cities:
        aqi = random.randint(20, 180)
        category = (
            "Good" if aqi <= 50 else
            "Moderate" if aqi <= 100 else
            "Unhealthy for Sensitive Groups" if aqi <= 150 else
            "Unhealthy"
        )
        data.append({
            "city": name,
            "lat": lat,
            "lon": lon,
            "aqi": aqi,
            "category": category,
        })
    return data
