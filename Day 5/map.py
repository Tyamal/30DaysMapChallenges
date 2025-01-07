import geopandas as gpd
import matplotlib.pyplot as plt

# Load the world shapefile (GeoDataFrame)
world = gpd.read_file(gpd.datasets.get_path('naturalearth_lowres'))

# Calculate population density
world['pop_density'] = world['pop_est'] / world['area']

# Create a color map based on population density
# You can customize the colormap as needed
world['color'] = pd.cut(world['pop_density'], bins=5, labels=plt.cm.viridis(range(0, 256, 51)))

# Plotting
fig, ax = plt.subplots(1, 1, figsize=(15, 10))
world.boundary.plot(ax=ax, linewidth=1, color='black')  # Draw boundaries
world.plot(ax=ax, color=world['color'], legend=True)

# Add title and labels
plt.title('World Map Colored by Population Density', fontsize=15)
plt.xlabel('Longitude', fontsize=12)
plt.ylabel('Latitude', fontsize=12)

# Show the plot
plt.show()