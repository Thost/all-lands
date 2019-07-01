# Polygon merging SIMPLE
# Trevor Host, 05/08/2019

# Import arcpy module
import arcpy
import sys
import os
from arcpy import env
arcpy.env.overwriteOutput = True

start_time = time.time()

# pass input and output file names
# first arg, input directory
# second arg, height strata integer (2, 5, 10, 15, 20) 
# third arg, output file name (SHP) 
inFile = sys.argv[1]
strata = sys.argv[2]
outFile = sys.argv[3]

#inFile = "C:\Users\hostx009\Documents\temp"
#outFile = "C:\\Users\\hostx009\\Documents\\temp\\temp.shp"

# Local variables:
temp1 = "C:\\Users\\hostx009\\Documents\\ArcGIS\\Default1.gdb\\polyMerge_temp1"
temp2 = "C:\\Users\\hostx009\\Documents\\ArcGIS\\Default1.gdb\\polyMerge_temp2"

arcpy.env.workspace = inFile
List = arcpy.ListFeatureClasses("*clean.shp")

# Process: Merge
arcpy.Merge_management(List,temp1)

# Process: Eliminate Polygon Part
arcpy.EliminatePolygonPart_management(temp1, temp2, "AREA", "5000 SquareMeters", "", "CONTAINED_ONLY")

# Process: add z field
arcpy.AddField_management(temp2, "z", "LONG", "", "", "", "", "NULLABLE", "NON_REQUIRED", "")

# Process: Calculate Field
arcpy.CalculateField_management(temp2, "z", strata, "VB", "")

# Process: Polygon to raster
arcpy.PolygonToRaster_conversion(temp2, "z", outFile, "CELL_CENTER", "NONE", "1")

# # Process: Delete
arcpy.Delete_management(temp1, "")
arcpy.Delete_management(temp2, "")

# report time
elapsed_min = (time.time() - start_time)/60
print elapsed_min
