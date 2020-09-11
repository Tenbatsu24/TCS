def bubble(data):
    donesorting = False
    upper = len(data)-1
    while not(donesorting):
        donesorting = True
        for i in range(0, upper):
            if data[i] > data[i+1]:
                data[i], data[i+1] = data[i+1], data[i]
                donesorting = False
        upper -= 1
    return data

def merge(data):
    length = len(data)
    if len(data) == 0 or len(data) == 1:
        return data
    else:
        fst = merge(data[0:(length//2)])
        snd = merge(data[(length//2):length])
        res = []
        fi = 0
        si = 0
        while fi < len(fst) and si < len(snd):
            if fst[fi] < snd[si]:
                res.append(fst[fi])
                fi += 1
            else:
                res.append(snd[si])
                si += 1
        if fi < len(fst):
            res.extend(fst[fi:len(fst)])
        else:
            res.extend(snd[si:len(snd)])
    return res

def merge_pairs(data):
    length = len(data)
    if len(data) == 0 or len(data) == 1:
        return data
    else:
        fst = merge(data[0:(length//2)])
        snd = merge(data[(length//2):length])
        res = []
        fi = 0
        si = 0
        while fi < len(fst) and si < len(snd):
            if (fst[fi][0] < snd[si][0]) or ((fst[fi][0] == snd[si][0]) and (fst[fi][1] < snd[si][1])):
                res.append(fst[fi])
                fi += 1
            else:
                res.append(snd[si])
                si += 1
        if fi < len(fst):
            res.extend(fst[fi:len(fst)])
        else:
            res.extend(snd[si:len(snd)])
    return res

def bubbledes(data):
    donesorting = False
    upper = len(data)-1
    while not(donesorting):
        donesorting = True
        for i in range(0, upper):
            if (data[i][1] < data[i+1][1]) or ((data[i][1] == data[i+1][1]) and (data[i][0] > data[i+1][0])):
                data[i], data[i+1] = data[i+1], data[i]
                donesorting = False
        upper -= 1
    return data
