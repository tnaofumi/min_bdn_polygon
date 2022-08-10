# min_bdn_polygon
## Description
Takes input geojson file of polygons, calculates the minimum bounding rectangle 
of each polygon and saves the rectangle as individual geojson. It supports multiple 
polygons per file and will descriminate from other shape types. Files that span the 
anti-meridian in which some of the longitude is negative will lead to weird
behavior in most geojson viewers.     

## Inputs
Input file is required and is the first argument  
Input directory defaults to current work directory `--src_dir`. Defaults to script directory  
Output file defaults to input file with _min_bnd_rect_(number) `--dest_file`. Defaults to input filename_min_bnd_rect.json  
Output directory defaults to current work directory `--dest_dir` Defaults to script directory  

## Example command line initiation
#### Define all input 
`python minimum_bnd_polygon.py polygon_multi.json --src_dir C:\Users\nonli\PycharmProjects\bounding_rectangle --dest_dir C:\Users\nonli\PycharmProjects --dest_file polygon.json`

#### Define input directory and file
`python minimum_bnd_polygon.py polygon_multi.json --src_dir C:\Users\nonli\PycharmProjects\bounding_rectangle`


