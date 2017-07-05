""" words function takes string and returns occurances for each word """
def words(long_string):
    """ takes string and returns occurances for each word """
    string_list = long_string.split()
    output = {}
    for string in set(string_list):
        if string.isdigit():
            output[int(string)] = string_list.count(string)
        else:
            output[string] = string_list.count(string)
    return output
