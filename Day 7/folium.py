import folium

# Create a base map centered on Indonesia
indonesia_map = folium.Map(location=[-5.0, 120.0], zoom_start=5)  # Centered on Indonesia

# Define industries and their locations
industries = [
    {"name": "Palm Oil Industry", "coordinates": [-1.5, 103.5], "info": "Major palm oil production area."},
    {"name": "Textile Industry", "coordinates": [-6.2, 106.8], "info": "Textile manufacturing hub in Jakarta."},
    {"name": "Tourism Industry", "coordinates": [-8.5, 115.2], "info": "Popular tourist destination in Bali."},
    {"name": "Mining Industry", "coordinates": [-2.5, 140.7], "info": "Mining activities in Papua."},
    {"name": "Fishing Industry", "coordinates": [-5.4, 105.3], "info": "Fishing industry in Lampung."}
]

# Add markers to the map
for industry in industries:
    folium.Marker(
        industry["coordinates"],
        popup=f"<strong>{industry['name']}</strong><br>{industry['info']}",
        icon=folium.Icon(color='green')
    ).add_to(indonesia_map)

# Save the map to an HTML file
indonesia_map.save("mala_mapping_day7.html")

print("Map has been created and saved as 'mala_mapping_day7.html'.")