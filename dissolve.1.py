# Polygon dissolve for forest stand boundaries generated with LASboundary
# Trevor Host, 4/23/2019

# Import arcpy module
import arcpy
import sys
import os
from arcpy import env
arcpy.env.overwriteOutput = True

# pass input and output file names 
# works well with: for %f in (*.shp) do python.exe XXX.py %f %~nf_clean.shp 
inFile = sys.argv[1]
outFile = sys.argv[2]

# Debuggin
#inFile = "Y:\project\All_Lands\Data\stand_development\USGS_LPC_MN_Arrowhead_B2_2011_1142_30_35_LAS_2016_color_c6z10.shp"
#outFile = "Y:\project\All_Lands\Data\stand_development\USGS_LPC_MN_Arrowhead_B2_2011_1142_30_35_LAS_2016_color_c6z10_diss.shp"

# Local variables:
temp1 = "C:\\Users\\hostx009\\Documents\\ArcGIS\\Default1.gdb\\temp1"
temp2 = "C:\\Users\\hostx009\\Documents\\ArcGIS\\Default1.gdb\\temp2"
temp3 = "C:\\Users\\hostx009\\Documents\\ArcGIS\\Default1.gdb\\temp3"
temp4 = "C:\\Users\\hostx009\\Documents\\ArcGIS\\Default1.gdb\\temp4"
temp5 = "C:\\Users\\hostx009\\Documents\\ArcGIS\\Default1.gdb\\temp5"
temp6 = "C:\\Users\\hostx009\\Documents\\ArcGIS\\Default1.gdb\\temp6"
temp7 = "C:\\Users\\hostx009\\Documents\\ArcGIS\\Default1.gdb\\temp7"

# Process: Dissolve
arcpy.Dissolve_management(inFile, temp1, "", "", "SINGLE_PART", "DISSOLVE_LINES")

# Process: Eliminate Polygon Part
arcpy.EliminatePolygonPart_management(temp1, temp2, "PERCENT", "400 SquareMeters", "99", "CONTAINED_ONLY")

# Process: Select
arcpy.Select_analysis(temp2, temp3, "Shape_area>20000")

# Process: Buffer Erode
arcpy.Buffer_analysis(temp3, temp4,"-6 meters")

# Process: Buffer Dialate
arcpy.Buffer_analysis(temp4, temp5,"6 meters")

# Process: Dissolve
arcpy.Dissolve_management(temp5, temp6, "", "", "SINGLE_PART", "DISSOLVE_LINES")

# Process: Select
arcpy.Select_analysis(temp6, outFile, "Shape_area>20000")

# Process: Delete
arcpy.Delete_management(temp1, "")
arcpy.Delete_management(temp2, "")
arcpy.Delete_management(temp3, "")
arcpy.Delete_management(temp4, "")
arcpy.Delete_management(temp5, "")
arcpy.Delete_management(temp6, "")
arcpy.Delete_management(temp7, "")
