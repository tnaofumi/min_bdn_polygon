from geojson import load, Polygon, dump

class data_loaders():

    def load_geojson_coordinates(
            dir: (str, "directory and file being loaded")
    ):
        """
        Load geojson coordinates
        Arguments:
            dir: directory and file name of target geojson
        Returns:
            longitude and latitude of geojson as lists
        """

        with open(dir) as f:
            features_collection = load(f)

        return features_collection


    def save_geojson(
                    lon: (list, "list of floats"),
                     lat: (list, "list of floats"),
                     dir: (str, "directory and file being loaded")
            ):
        """
        Saves geojson coordinates
        Arguments:
            lon: list of floats that's the longitude
            lat: list of floats that's the latitude
            dir: directory and file name of target geojson
        Returns:
            saves coordinates as a geojson file
        """

        features = Polygon(list(zip(lon, lat)))

        with open(dir, 'w') as f:
            dump(features, f)






