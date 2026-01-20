import requests
import folium

# Step 1: Get geolocation from IP
def get_location():
    url = "http://ip-api.com/json/"
    response = requests.get(url)
    data = response.json()

    if data["status"] == "success":
        return {
            "ip": data["query"],
            "city": data["city"],
            "region": data["regionName"],
            "country": data["country"],
            "lat": data["lat"],
            "lon": data["lon"]
        }
    else:
        raise Exception("Unable to fetch location")

# Step 2: Create map
def create_map(location):
    m = folium.Map(location=[location["lat"], location["lon"]], zoom_start=10)

    folium.Marker(
        [location["lat"], location["lon"]],
        popup=f"""
        IP: {location['ip']}<br>
        City: {location['city']}<br>
        Region: {location['region']}<br>
        Country: {location['country']}
        """,
        tooltip="User Location"
    ).add_to(m)

    m.save("user_location_map.html")
    print("Map saved as user_location_map.html")

# Main
if __name__ == "__main__":
    location = get_location()
    print("Location fetched:")
    for k, v in location.items():
        print(f"{k}: {v}")

    create_map(location)
