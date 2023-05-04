import arcpy
from arcpy import env
from arcpy.sa import *

'''
This is a model to convert point shp file to kriging raster, clip the raster by geographic boundaries, and then convert raster to point shape file.
'''



def Model():

    # To allow overwriting outputs change overwriteOutput option to True.
    arcpy.env.overwriteOutput = True

    # check out the ArcGIS Spatial Analyst extention license
    arcpy.CheckOutExtension("Spatial")

    # Set complex variables
    copd_point_shp = "\\path"
    lagSize = 0.0486
    majorRange = 0.3889
    partialSill = 3.515
    nugget = 1.932
    kModelOrdinary = KrigingModelOrdinary("EXPONENTIAL", lagSize, majorRange, partialSill, nugget)

    # Process: Kriging
    Output_variance_raster = "\\path"
    Kriging_map = arcpy.sa.Kriging(copd_point_shp, "Data_Val_1", kModelOrdinary, "1.06547447600001E-02", "VARIABLE 12", Output_variance_raster)
    Kriging_map.save("\\path")


    #Clip rater by state boundaries
    Krig_raster = arcpy.Raster("\\path")
    boundaries= "\\path"
    
    # Process: Clip Raster
    Krig_clip = "\\path"
    arcpy.management.Clip(in_raster=Krig_copd_raster, rectangle="-84.321869118301 33.8417557488691 -75.4600346316926 36.5881560102784",
                          out_raster=Krig_copd_Clip, in_template_dataset=NC_State_Boundaries, nodata_value="3.4e+38",
                          clipping_geometry="ClippingGeometry", maintain_clipping_extent="NO_MAINTAIN_EXTENT")
    Krig_clip = arcpy.Raster(Krig_clip)


    # Process: Raster to Point
    Krig_point = "\\path"
    arcpy.conversion.RasterToPoint(in_raster=Krig_Clip, out_point_features=Krig_point, raster_field="Value")


if __name__ == '__main__':
    # Global Environment settings
    # If remove this line, the created raster will only present black and white, so I recommend to save the file under the gdb file.
    
    with arcpy.EnvManager(scratchWorkspace=r"\\path", workspace=r"\\path"):
        Model()
