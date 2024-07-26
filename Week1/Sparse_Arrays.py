# ----- Type-1 ------
def matchingStrings(strings, queries):
    # Write your code here
    result_string = []
    dict_string = {item: 0 for item in queries}
    for values in strings:
        if values in dict_string:
            dict_string[values] += 1
    for values in queries:
        result_string.append(dict_string.get(values))
    return result_string

# ----- Type-2 ------
def matchingStrings(strings, queries):
    # Write your code here
    result, string = [], {}
    for s in strings:
        if s in string:
            string[s] += 1
        else:
            string[s] = 1
            
    for q in queries:
        if q in string:
            result.append(string[q])
        else:
            result.append(0)
            
    return result

# ----- Type-3 ------
def matchingStrings(strings, queries):
    # Write your code here
    result = []
    for value in queries:
        list = [element for element in strings if element == value]
        result.append(len(list))
    
    return result