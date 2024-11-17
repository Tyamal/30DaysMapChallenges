# Load library yang dibutuhkan
library(sf)
library(ggplot2)
library(rnaturalearth)
library(rnaturalearthdata)

# Unduh data peta Indonesia dari Natural Earth
indonesia <- ne_countries(scale = "medium", country = "Indonesia", returnclass = "sf")

# Ambil batas wilayah Pulau Jawa berdasarkan koordinat
# (Gunakan bounding box yang sesuai untuk Pulau Jawa)
pulau_jawa_bbox <- st_bbox(c(xmin = 105, xmax = 115, ymin = -9, ymax = -5), crs = 4326)

# Potong wilayah Indonesia hanya pada Pulau Jawa
pulau_jawa <- st_crop(indonesia, pulau_jawa_bbox)

# Plot peta Pulau Jawa
ggplot(data = pulau_jawa) +
  geom_sf(fill = "lightblue", color = "black") +
  theme_minimal() +
  ggtitle("Peta Pulau Jawa") +
  theme(plot.title = element_text(hjust = 0.5, size = 16))
