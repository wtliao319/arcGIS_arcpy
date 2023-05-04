import arcpy
from arcpy.sa import *

'''
This is a pyhton script to extract multipe point values from raster with point shape file.
'''


# Set the workspace
arcpy.env.workspace = "\\path"

# To allow overwriting outputs change overwriteOutput option to True.
arcpy.env.overwriteOutput = True


# check out the ArcGIS Spatial Analyst extention license
arcpy.CheckOutExtension("Spatial")

# Set the input point shapefile and raster file
point_shapefile = "\\path"
raster_file = "\\path"

# Set the output feature class for the extracted values
output_feature_class = "\\path"

# Use the ExtractValuesToPoints function to extract the raster values at the points
arcpy.sa.ExtractValuesToPoints(point_shapefile, raster_file, output_feature_class)
