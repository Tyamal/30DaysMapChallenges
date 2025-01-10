# Create a buffer around geometries
gdf['buffered'] = gdf.geometry.buffer(0.01)  # Buffer by 0.01 degrees
gdf['buffered'].plot(color='none', edgecolor='red')
plt.show()
