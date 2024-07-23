# ----- Type-1 ------
def timeConversion(temp_str):
    # Write your code here
    array = temp_str.split(":")

    if "AM" in temp_str:
        if array[0] == "12":
            array[0] = "00"
    else:
        if array[0] != "12":
            array[0] = str(12+int(array[0]))
    array[2] = array[2][:2]

    return ":".join(array)

# ----- Type-2 ------
def timeConversion(temp_str):
    hours = int(temp_str.split(":")[0])
    if temp_str.endswith('AM'):
        if hours == 12:
            num = "00"
        else: 
            if hours == 12:
                num = temp_str[0:2]
    else:
        if hours == 12:
            num = "12"
        else:
            num = str(num + 12)

    return num + temp_str[2:8]

# ----- Type-3 ------
def timeConversion(temp_str):
    time = temp_str[-2]
    if time == 'PM' and temp_str[:2] != '12':
        temp_str = str(12 + int(temp_str[:2])) + temp_str[2:]
    if time == 'AM' and temp_str[:2] == '12':
        temp_str = '00' + temp_str[2:]
        
    return temp_str[:-2]