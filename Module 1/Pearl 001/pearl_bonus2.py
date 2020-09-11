import sort                                                         #imports merge sort and bubbledes
import ordsearch
import dup                                                          #imports count_dupes_per_file, merge_dupes_file
import util

def make_table(pairs):
    ref = count_files_words(pairs)                                  #make a table which keeps in track the number of wrods in each file
    result1 = sort.merge_pairs(pairs)                               #merge sort the pairs
    result2 = dup.count_dupes_per_file(result1)                     #count the number of duplicates for each word in each file
    result3 = dup.merge_dupes_file(result2)                         #make a list for each word listing all the files they occur in
    for i in range(0,len(result3)):                                 #calculates the frequency density for each word in each file using the list created above
            result3[i][1] = calculate_density(result3[i][1], ref)   #carries out the function above for each i-th word
    result3 = make_des(result3)                                     #makes it descending order
    return result3                                                  #gives back the result

def count_files_words(pairs):
        ref = []                                                    #makes an empty list to keep track of number of words for each file
        fileindex = 0
        fresh = pairs[0]                                            #sets the file name as fresh, the first encountered file name is always the one that has not yet been repeated ie fresh
        ref.append([fresh[1], 1])                                   #keeps track of file name and number of wrods as a pair, ["filename", no. of words]
        for i in range(0,len(pairs)):
                if pairs[i][1] == fresh[1]:                         #if the filename in pairs is same as fresh,
                        ref[fileindex][1] += 1                      #increment counter of the number of words
                else:                                               #new file name has been encountred
                        fileindex += 1                              #ref index is incremented for the new filename
                        fresh = pairs[i]                            #make the pair filename fresh and repeat as for the first fresh element
                        ref.append([fresh[1], 1])
        return ref                                                  #give back the data

def calculate_density(pairs, ref):
        for i in range(0,len(pairs)):                               #do the below for all list that was input for a specific word
                found = False                                       #flag for if the file name is found in the ref array for the corresponding filename in the pair input
                j = 0
                value = 1
                while not(found) and j<len(ref):                    #continoues to look for the filename until found in ref and j has not reached out of list
                        if pairs[i][0] == ref[j][0]:                #is the filename same as the one we are looking for
                                found = True                        #if so, set found=True
                                value = ref[j][1]                   #value set to the number of words in the file that was stored in the ref also as a pair
                        else:
                                j += 1                              #not a match go to next element
                pairs[i][1] = round((pairs[i][1]/value),7)          #calculate frequency density using found value to seven decimal places
        return pairs                                                #return the result

def make_des(result):                                               #uses bubble sort to make the list into descending order
    for i in range(0,len(result)):
            result[i][1] = sort.bubbledes(result[i][1])
    return result
