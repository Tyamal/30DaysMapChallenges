import json
import sqlite3  # or any other database connector

# Connect to your database
conn = sqlite3.connect('mining_data.db')
cursor = conn.cursor()

# Execute the SQL query
cursor.execute('''
    SELECT site_id, site_name, latitude, longitude, mineral_type 
    FROM mining_sites 
    WHERE active = 1;
''')

# Fetch all results
rows = cursor.fetchall()

# Transform data into GeoJSON format
features = []
for row in rows:
    feature = {
        "type": "Feature",
        "geometry": {
            "type": "Point",
            "coordinates": [row[3], row[2]]  # [longitude, latitude]
        },
        "properties": {
            "site_id": row[0],
            "site_name": row[1],
            "mineral_type": row[4]
        }
    }
    features.append(feature)

geojson = {
    "type": "FeatureCollection",
    "features": features
}

# Save GeoJSON to a file
with open('mining_sites.geojson', 'w') as f:
    json.dump(geojson, f)

# Close the database connection
conn.close()