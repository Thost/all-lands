# All-lands

Stand boundaries generated from lidar  
data-driven, human-used

# Workflow

For each height strata (z2, z5, z10, z15, z20)  
1. LASboundary - generate shapefile boundary  
  Concave Hull - concavity 20 m  
  Buffered 20 m  
  *parallel*
```cmd  
:: where %z% is an integer height strata
:: and %LAZ% is the directory path containing the point cloud tiles
  lasboundary 
    -i %LAZ%\*.laz 
    -concavity 20 
    -keep_z_above %z% 
    -disjoint 
    -holes 
    -odix _c20z%z% 
    -drop_classification 17 
    -buffered 20 
    -odir result\z%z%
```
2. polyDissolve.v1 - clean up shapefile edges  
  Dissolve on tiles  
  *parallel*
3. polyMerge.v3 - merge shapefile tiles into one  
  Merge overlapping polygons  
  Remove donut polygons  
  Add z field and populate
  polygon to raster
4. Polygon flattening -  top-down layer stacking of height layers  
  layer stacking  
  Mosaic to new raster, keep maximum  
5. Clean up
  focal statistics - 10x10 majority filter  
  Raster to polygon    


