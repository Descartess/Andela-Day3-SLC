def words(string):
  """ takes string and returns occurances for each word """
  string_list = string.split()
  output = {}
  for string in set(string_list):
    if string.isdigit():
      output[int(string)] = string_list.count(string)
    else:
      output[string] = string_list.count(string)
  return output