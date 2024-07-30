# ----- Type-1 ------
import sys

def camelCase(line):
    arr = line.strip().split(";")
    operation = arr[0]
    command_type = arr[1]
    string = arr[2]
    if operation == 'S':
        if command_type == 'V':
            result = ''
            for i in range(len(string)):
                if string[i].isupper():
                    result += " " + string[i].lower()
                else:
                    result += string[i]
            print(result)
        elif command_type == 'C':
            result = string[0].lower()
            for i in range(1, len(string)):
                if string[i].isupper():
                    result += " " + string[i].lower()
                else:
                    result += string[i]
            print(result)
        else:
            result = string[0]
            for i in range(1, len(string)):
                if string[i].isupper():
                    result += " " + string[i].lower()
                else:
                    result += string[i]
            print(result[:len(result)-2])
    else:
        str_arr = string.split(" ")
        if command_type == 'M':
            for i in range(len(str_arr)):
                if i!=0:
                    str_arr[i] = str_arr[i].capitalize()
            print("".join(str_arr) + "()")
        elif command_type == 'C':
            for i in range(len(str_arr)):
                str_arr[i] = str_arr[i].capitalize()
            print("".join(str_arr))
        else:
            for i in range(len(str_arr)):
                if i!= 0:
                    str_arr[i] = str_arr[i].capitalize()
            print("".join(str_arr))

if __name__ == '__main__':
    for line in sys.stdin:
        camelCase(line.strip())