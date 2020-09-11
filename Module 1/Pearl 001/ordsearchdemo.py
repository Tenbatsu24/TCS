import time

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

data = []
for i in range(0,20000):
    data.append(i)

x = int(round(time.time() * 1000))
print(linear(data,20000))
y = int(round(time.time() * 1000))
print(y-x)

x = int(round(time.time() * 1000))
print(binary(data,20000))
y = int(round(time.time() * 1000))
print(y-x)

print()
print()

order = [1,2,3,5,6,7]
unord = [2,5,6,1,4,0]
mix = [1,2,3,4,"a","b","c"]

print("expected: 2", ordsearch(order,3))
print("expected: 2", ordsearch(order,4))
print()
print()
print(ordsearch(unord,1))
print(ordsearch(unord,9))
print(ordsearch(mix,4))
print()
print("Binary: ")
print("expected: 2")
x = binarysearch(order,3)
print(x)
print("expected: 5")
y = binarysearch(order,7)
print(y)


