import argparse
import os
from geometry_calculations.boundary_calculations import minimum_bounding_rectangle
from save_load_data.save_load_data import load_geojson, save_geojson

def export_min_bnd_json(in_dir, in_filename, out_dir, out_filename):

    features = load_geojson(in_dir + "\\" + in_filename)

    ##Code for single feature files
    if features["type"] == "Polygon":
        lon = [item[0] for item in features["coordinates"][0]]
        lat = [item[1] for item in features["coordinates"][0]]

        bnd_lon, bnd_lat = minimum_bounding_rectangle(lon, lat)

        save_geojson(bnd_lon, bnd_lat, out_dir, out_filename, "", ".json")

    if features["type"] == "LineString" or features["type"] == "Point":
        raise RuntimeError("No polygons in geojson file")

    ##main loop for FeatureCollection JSON's
    if features["type"] == "FeatureCollection":
        n = 0 #indexes so if no polygons in collection a error can be triggered

        for m in range(features["features"].__len__()):
            if features[m]["geometry"]["type"] == "Polygon":
                lat = [item[1] for item in features[m]["geometry"]["coordinates"][0]]
                lon = [item[0] for item in features[m]["geometry"]["coordinates"][0]]

                bnd_lon, bnd_lat = minimum_bounding_rectangle(lon, lat)

                save_geojson(bnd_lon, bnd_lat, out_dir, out_filename, m,".json", )

            else:
                print("The " + str(m + 1) + " in the feature collection is not a polygon")
                n += 1

        if n == features["features"].__len__():
            raise RuntimeError("No polygons in geojson file")

if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='''
                Takes input geojson file of polygons, calculates the minimum bounding rectangle 
                of each polygon and saves the rectangle as individual geojson. It supports multiple 
                polygons per file and will descriminate from other shape types. Files that span the 
                anti-meridian in which some of the longitude is greatly negative will lead to weird
                behavior in some geojson viewers.     
            --------------------------------
                Input file is required
                Input directory defaults to current work directory
                Output file defaults to input file with _min_bnd_rect_(number)
                Output directory defaults to current work directory
            ''', formatter_class=argparse.RawTextHelpFormatter)

    ###############  add behavior to save property name as file name

    #parser.add_argument("--src_file", type=str, help="Input  file", required = False)
    parser.add_argument("src_file", type=str, help="Input  file")
    parser.add_argument("--src_dir", nargs='?', default=os.getcwd(), type = str, help="Input directory", required = False)
    parser.add_argument("--dest_file", type=str, default = "default", help="Output file", required = False)
    parser.add_argument("--dest_dir", nargs='?', default=os.getcwd(), type=str, help="Output directory", required = False)

    args = parser.parse_args()
    #args.src_file = "mixed_geometries.json"
    #args.src_dir = r"C:\Users\nonli\PycharmProjects"

    ##handles setting default values incase of missing file name output
    if args.dest_file == "default":
        if "." in args.src_file:
            args.dest_file = args.src_file[:args.src_file.find(".")] + "_min_bnd_rect" + args.src_file[args.src_file.find("."):]
        else:
            args.dest_file = args.src_file[:args.src_file.find(".")] + "_min_bnd_rect.json"
    export_min_bnd_json(args.src_dir, args.src_file, args.dest_dir, args.dest_file)

