import arcpy

# Set the workspace to your geodatabase
arcpy.env.workspace = r"C:\path\to\your\geodatabase.gdb"

# Define input feature classes
geological_units = "GeologicalUnits"  # Feature class with geological units
mining_sites = "MiningSites"           # Feature class with mining site locations
output_map = "MiningGeologyMap"        # Output map document

# Create a new map document
mxd = arcpy.mapping.MapDocument("CURRENT")

# Add geological units to the map
geological_layer = arcpy.mapping.Layer(geological_units)
arcpy.mapping.AddLayer(mxd.activeView, geological_layer)

# Add mining sites to the map
mining_layer = arcpy.mapping.Layer(mining_sites)
arcpy.mapping.AddLayer(mxd.activeView, mining_layer)

# Set symbology for geological units
arcpy.ApplySymbologyFromLayer_management(geological_layer, r"C:\path\to\symbology\GeologicalUnitsSymbology.lyr")

# Set symbology for mining sites
arcpy.ApplySymbologyFromLayer_management(mining_layer, r"C:\path\to\symbology\MiningSitesSymbology.lyr")

# Zoom to the extent of the geological units
extent = geological_layer.getExtent()
mxd.activeView.extent = extent

# Save the map document
mxd.saveACopy(r"C:\path\to\output\MiningGeologyMap.mxd")

# Clean up
del mxd
del geological_layer
del mining_layer

print("Mapping completed successfully!")