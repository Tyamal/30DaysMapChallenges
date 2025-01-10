from sklearn.cluster import KMeans
import numpy as np

# Assuming 'coordinates' is a DataFrame with latitude and longitude
kmeans = KMeans(n_clusters=3)
kmeans.fit(coordinates)

# Add cluster labels to the DataFrame
coordinates['cluster'] = kmeans.labels_
