# All-lands

Stand boundaries generated from lidar  
data-driven, human-used

# Workflow
Initial point cloud normalization
LASheight: Normalize point cloud by ground elevation, z values = height above ground
```cmd
lasheight -i *.laz -replace_z -buffered 5 -class 2 8 -olaz -odix _z -cores 15
```
-replace_z option
On-the-fly buffered 5 m to avoid edge effects


For each height strata (z2, z5, z10, z15, z20)  
1. LASheight: Normalize point cloud by ground elevation, z values = height above ground  
  replace_z option  
  On-the-fly buffered 5 m to avoid edge effects  
2. LASboundary - generate shapefile boundary  
  Concave Hull - concavity 20 m  
  Buffered 20 m  
  *parallel*
```cmd  
:: where %z% is an integer height strata
:: and %LAZ% is the directory path containing the point cloud tiles
  lasboundary ^
    -i %LAZ%\*.laz ^ 
    -concavity 20 ^
    -keep_z_above %z% ^ 
    -disjoint ^
    -holes ^
    -odix _c20z%z% ^ 
    -drop_classification 17 ^
    -buffered 20 ^
    -odir result\z%z%
```
3. polyDissolve.v1 - clean up shapefile edges  
  Dissolve on tiles  
  *parallel*
4. polyMerge.v3 - merge shapefile tiles into one  
  Merge overlapping polygons  
  Remove donut polygons  
  Add z field and populate
  polygon to raster
5. Polygon flattening -  top-down layer stacking of height layers  
  layer stacking  
  Mosaic to new raster, keep maximum  
6. Clean up  
  focal statistics - 10x10 majority filter  
  Raster to polygon  
  Eliminate polygon part 99 percent
7. Attribution  
  Calculating canopy metrics (full list below)  
  MRFD yr_onset - Zonal statistics to table: Majority and Count  
  Join tables to polygon by OBJECTID  


