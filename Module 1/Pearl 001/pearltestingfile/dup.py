def remove_dup(data):
    res = []
    if len(data) != 0:
        fresh = data[0]
        i = 1
        while i < len(data):
            if data[i] != fresh:
                res.append(fresh)
                fresh = data[i]
            i += 1
        res.append(fresh)
    return res

def merge_dupes_file(data):
    res= []
    newindex = 0
    new = data[0][0]
    res.append([new,[data[0][1]]])
    for i in range(1,len(data)):
        if data[i][0] == new:
            res[newindex][1].append(data[i][1])
        else:
            new = data[i][0]
            res.append([new,[data[i][1]]])
            newindex += 1
    return res
        
def count_dupes_per_file(data):
    res= []
    newindex = 0
    new = data[0]
    res.append([new[0],[data[newindex][1], 1]])
    for i in range(1,len(data)):
        if data[i] == new:
            res[newindex][1][1] = res[newindex][1][1] + 1
        else:
            new = data[i]
            newindex += 1
            res.append([new[0],[data[i][1], 1]])
    return res
