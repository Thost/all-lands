# Polygon merging
# Trevor Host, 4/24/2019

# Import arcpy module
import arcpy
import sys
import os
from arcpy import env
arcpy.env.overwriteOutput = True

start_time = time.time()

# pass input and output file names 
inFile = sys.argv[1]
outFile = sys.argv[2]

#inFile = "C:\Users\hostx009\Documents\temp"
#outFile = "C:\\Users\\hostx009\\Documents\\temp\\temp.shp"

# Local variables:
temp = "C:\\Users\\hostx009\\Documents\\ArcGIS\\Default1.gdb"
temp1 = "C:\\Users\\hostx009\\Documents\\ArcGIS\\Default1.gdb\\polyMerge_temp1"
temp2 = "C:\\Users\\hostx009\\Documents\\ArcGIS\\Default1.gdb\\polyMerge_temp2"
temp3 = "C:\\Users\\hostx009\\Documents\\ArcGIS\\Default1.gdb\\polyMerge_temp3"
temp4 = "C:\\Users\\hostx009\\Documents\\ArcGIS\\Default1.gdb\\polyMerge_temp4"
temp5 = "C:\\Users\\hostx009\\Documents\\ArcGIS\\Default1.gdb\\polyMerge_temp5"
temp6 = "C:\\Users\\hostx009\\Documents\\ArcGIS\\Default1.gdb\\polyMerge_temp6"
temp7 = "C:\\Users\\hostx009\\Documents\\ArcGIS\\Default1.gdb\\polyMerge_temp7"

arcpy.env.workspace = inFile
List = arcpy.ListFeatureClasses()

# Dissolve each tile AS OUTPUT FROM LASTOOLS, merging first will cause errors in the output polygons, dissolve needs to be the first step
for fc in List:
    arcpy.Dissolve_management(fc, os.path.join(inFile, os.path.splitext(fc)[0] + "_clean.shp"), "", "", "SINGLE_PART", "DISSOLVE_LINES")

List = arcpy.ListFeatureClasses("*clean.shp")
# Process: Merge
arcpy.Merge_management(List,temp1)

# Process: Select
arcpy.Select_analysis(temp1, temp2, "Shape_area>1000")

# Process: Dissolve
arcpy.Dissolve_management(temp2, temp3, "", "", "SINGLE_PART", "DISSOLVE_LINES")

# Process: Eliminate Polygon Part
arcpy.EliminatePolygonPart_management(temp3, temp4, "AREA", "5000 SquareMeters", "", "CONTAINED_ONLY")

# Process: Select
arcpy.Select_analysis(temp4, temp5, "Shape_area>5000")

# Process: Dissolve
arcpy.Dissolve_management(temp5, outFile, "", "", "SINGLE_PART", "DISSOLVE_LINES")

# Process: Delete
arcpy.Delete_management(temp1, "")
arcpy.Delete_management(temp2, "")
arcpy.Delete_management(temp3, "")
arcpy.Delete_management(temp4, "")
arcpy.Delete_management(temp5, "")
arcpy.Delete_management(temp6, "")
arcpy.Delete_management(temp7, "")

# report time
elapsed_time = time.time() - start_time
print elapsed_time

