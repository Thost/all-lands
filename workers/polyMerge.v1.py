# Polygon merging
# Trevor Host, 4/24/2019

# Import arcpy module
import arcpy
import sys
import os
from arcpy import env
arcpy.env.overwriteOutput = True

# pass input and output file names 
inFile = sys.argv[1]
outFile = sys.argv[2]

#inFile = "C:\Users\hostx009\Documents\temp"
#outFile = "C:\\Users\\hostx009\\Documents\\temp\\temp.shp"

# Local variables:
temp1 = "C:\\Users\\hostx009\\Documents\\ArcGIS\\Default1.gdb\\temp1"

arcpy.env.workspace = inFile
List = arcpy.ListFeatureClasses()  

# Process: Merge
arcpy.Merge_management(List,temp1)

# Process: Dissolve
arcpy.Dissolve_management(temp1, outFile, "", "", "SINGLE_PART", "DISSOLVE_LINES")

# Process: Delete
arcpy.Delete_management(temp1, "")

