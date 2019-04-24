# All-lands

Stand boundaries generated from lidar  
data-driven, human-used

# Workflow

For each height strata (z2, z5, z10, z15, z20)  
1. LASboundary - generate shapefile boundary  
  *Concave Hull - concavity 6 m  
  *Buffered 20 m  
2. polyMorph.v1 - clean up shapefile edges 
  Dissolve  
  Remove donut polygons  
  Remote small polygons <5 acres  
  -buffer/buffer routine for morphology  
3. polyMerge.v1 - merge shapefile tiles into one  
  Merge overlapping polygons  
  Dissolve  
4. Final step: Flatten height strata to single layer
