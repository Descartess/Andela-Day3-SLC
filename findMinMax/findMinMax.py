def find_min_max(arr):
    """returns max and min values in list"""
    if min(arr) == max(arr):
        return [min(arr)]
    return [min(arr), max(arr)]
