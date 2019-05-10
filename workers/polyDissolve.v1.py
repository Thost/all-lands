# Polygon dissolve on tiles
# Trevor Host, 05/07/2019

# Import arcpy module
import arcpy
import sys
import os
from arcpy import env
arcpy.env.overwriteOutput = True

start_time = time.time()

# pass input and output file names 
inFile = sys.argv[1]

arcpy.env.workspace = inFile
List = arcpy.ListFeatureClasses("*.shp")

# Dissolve each tile AS OUTPUT FROM LASTOOLS, merging first will cause errors in the output polygons, dissolve needs to be the first step
for fc in List:
    arcpy.Dissolve_management(fc, os.path.join(inFile, os.path.splitext(fc)[0] + "_clean.shp"), "", "", "SINGLE_PART", "DISSOLVE_LINES")

# report time
elapsed_time = (time.time() - start_time)/60
print elapsed_time
