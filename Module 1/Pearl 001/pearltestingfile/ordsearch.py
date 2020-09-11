def linear(data,value):
    i = 0
    while ((i < len(data)) and (data[i] < value)):
        i += 1

    if i == len(data):
        return -1
    elif data[i] == value:
        return i
    else:
        return -1

def binary(data,value):
    lower = 0
    found = False
    upper = len(data) - 1
    while lower <= upper and not(found):
        mid = (lower+upper)//2
        if data[mid] == value:
            found = True
        elif data[mid] < value:
            lower = mid + 1
        else:
            upper = mid - 1
    if found:
        return mid
    else:
        return -1

def binary_pairs(data, value):
    lower = 0
    found = False
    upper = len(data) - 1
    while lower <= upper and not(found):
        mid = (lower+upper)//2
        if data[mid][0] == value:
            found = True
        elif data[mid][0] < value:
            lower = mid + 1
        else:
            upper = mid - 1
    if found:
        return mid
    else:
        return -1
