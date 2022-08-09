import argparse
from data_loaders.data_loaders import data_loaders
from geometry_calculations.boundary_calculations import boundary_calculation
import os

def export_min_bnd_json(in_dir, in_filename, out_dir, out_filename):

    features = data_loaders.load_geojson_coordinates(in_dir + "\\" + in_filename)

    ##main loop for FeatureCollection JSON's
    if features["type"] == "FeatureCollection":
        n = 0 #indexes so if no polygons in collection a error can be triggered

        for _ in range(features["features"].__len__()):
            if features[0]["geometry"]["type"] == "Polygon":
                lat = [item[1] for item in features[_]["geometry"]["coordinates"][0]]
                lon = [item[0] for item in features[_]["geometry"]["coordinates"][0]]

                bnd_lon, bnd_lat = boundary_calculation.minimum_bounding_rectangle(lon, lat)

                if "." in out_filename:
                    outfile_name = out_filename[:out_filename.find(".")] + "_" + str(_ + 1) + out_filename[out_filename.find("."):]
                else:
                    outfile_name = out_filename  + "_" + str(_ + 1) + ".json"

                out_file_str = out_dir + "\\" + outfile_name
                data_loaders.save_geojson(bnd_lon, bnd_lat, out_file_str)

            else:
                print("The " + str(_ + 1) + "in the feature collection is not a polygon")
                n += 1

        if n == range(features["features"].__len__()):
            raise RuntimeError("No polygons in geojson file")

    ##Code for single feature files
    if features["type"] == "Polygon":
        bnd_lon = [item[0] for item in features["coordinates"][0]]
        bnd_lat = [item[1] for item in features["coordinates"][0]]

        out_file_str = out_dir + "\\" + out_filename
        data_loaders.save_geojson(bnd_lon, bnd_lat, out_file_str)

    else:
        raise RuntimeError("No polygons in geojson file")

if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='''
                Takes input geojson file of polygons, calculates the minimum bounding rectangle 
                of each polygon and saves the rectangle as individual geojson. It supports multiple 
                polygons per file as well polygons spanning the meridian and anti-meridian.  
            --------------------------------
                Input file is required
                Input directory defaults to current work directory
                Output file defaults to input file with _min_bnd_rect_(number)
                Output directory defaults to current work directory
            ''', formatter_class=argparse.RawTextHelpFormatter)

    ############### Need to fix input directory input, add behavior to save property name as file name, and move file name
    ############### handler to seperate function?
    
    parser.add_argument("src_file", type=str, help="Input  file")
    parser.add_argument("--src_dir", nargs='?', default=os.getcwd(), type = str, help="Input directory", required = False)
    parser.add_argument("--dest_file", type=str, default = "default", help="Output file", required = False)
    parser.add_argument("--dest_dir", nargs='?', default=os.getcwd(), type=str, help="Output directory", required = False)

    args = parser.parse_args()

    ##handles setting default values incase of missing inputs
    if args.dest_file == "default":
        if "." in args.src_file:
            args.dest_file = args.src_file[:args.src_file.find(".")] + "_min_bnd_rect" + args.src_file[args.src_file.find("."):]
        else:
            args.dest_file = args.src_file[:args.src_file.find(".")] + "_min_bnd_rect.json"

    if args.dest_dir == os.getcwd() and args.dest_dir != args.src_dir:
        args.dest_dir = args.src_dir

    if args.src_dir == os.getcwd() and args.dest_dir != args.src_dir:
        args.src_dir = args.dist_dir

    export_min_bnd_json(args.src_dir, args.src_file, args.dest_dir, args.dest_file)

