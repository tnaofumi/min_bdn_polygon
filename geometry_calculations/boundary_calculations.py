def minimum_bounding_rectangle(
        lon: (list, "list of floats"),
         lat: (list, "list of floats"),
       ):
    """
    Calculates the minimum bounding polygon from arbitraty polygon
    Arguments:
        lon: list of floats that's the longitude
        lat: list of floats that's the latitude
    Returns:
        longitude and latitude lists of mimumum bounding polygon
    """

    min_lon = min(lon)
    max_lon = max(lon)
    min_lat = min(lat)
    max_lat = max(lat)

    bnd_lon = [min_lon, min_lon, max_lon, max_lon, min_lon]
    bnd_lat = [min_lat, max_lat, max_lat, min_lat, min_lat]

    return bnd_lon, bnd_lat


