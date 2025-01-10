import geopandas as gpd
import matplotlib.pyplot as plt

# Load a shapefile
gdf = gpd.read_file("path/to/your/shapefile.shp")

# Plot the geospatial data
gdf.plot(color='lightblue', edgecolor='black')
plt.title("Geospatial Data Visualization")
plt.show()
