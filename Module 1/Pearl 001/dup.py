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

def merge_dupes_file(data):                                 #checks duplicate words having different file name and puts them togethor
    res= []                                                 #new result list
    newindex = 0
    new = data[0][0]                                        #newest data, which has had no previous occurences in other files
    res.append([new,[data[0][1]]])                          #put this into a new list
    for i in range(1,len(data)):                            #starts from the next element
        if data[i][0] == new:                               #i-th data = data which previously had no occerences in other files?
            res[newindex][1].append(data[i][1])             #if yes put filename into the list associated with that word
        else:                                               #ooh, new, 'new' a different word with no previous occurences in other files
            new = data[i][0]                                #make a seperate list for these, no mixing
            res.append([new,[data[i][1]]])                  #repeat
            newindex += 1
    return res                                              #give back the result
        
def count_dupes_per_file(data):
    res= []                                                 #new list for the result
    newindex = 0
    new = data[0]                                           #this is the data which has not yet been repeated
    res.append([new[0],[data[newindex][1], 1]])             #put that into the result list, since not yet repeated, with count one
    for i in range(1,len(data)):                            #start with next element
        if data[i] == new:                                  #i-th data same as new?
            res[newindex][1][1] = res[newindex][1][1] + 1   #increment duplicate counter that every word has
        else:                                               #new data
            new = data[i]                                   #set as new data
            newindex += 1                                   #increment the newindex so that the an error of incrementing the wrong counter does not occur. newindex always stays with the new data item
            res.append([new[0],[data[i][1], 1]])            #do the same as for the first new data
    return res                                              #give output
