from geojson import load, Polygon, dump, FeatureCollection


def append_file_extension(in_file, num, extension):
    """
    Appends extension and a file number to file name if needed
    Arguments:
        in_file: input file name
        num: file number
        extension: file extension to append
    Returns:
         file name with extension and number
    """
    if num != "":
        file_num = str("_") + str(num + 1)

    else:
        file_num = ""

    if "." in in_file:
        outfile_name = in_file[:in_file.find(".")] + file_num + in_file[in_file.find("."):]
    else:
        outfile_name = in_file + file_num + extension

    return outfile_name

def load_geojson(dir):
    """
    Load geojson file
    Arguments:
        dir: directory and file name of target geojson
    Returns:
        longitude and latitude of geojson as lists
    """

    with open(dir) as f:
        features_collection = load(f)

    return features_collection


def save_geojson(lon, lat, dir, filename, file_number, extension):
    """
    Saves geojson coordinates
    Arguments:
        lon: list of floats that's the longitude
        lat: list of floats that's the latitude
        dir: output directory
        file_name: base output file name
        file_number: file number to append if desired
        extension: file extension
    Returns:
        saves coordinates as a geojson file
    """

    out_str = dir + "\\" +append_file_extension(filename, file_number, extension)

    features = Polygon([list(zip(lon, lat))])

    with open(out_str, 'w') as f:
        dump(features, f, indent=4)






