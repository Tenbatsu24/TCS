import sort
import ordsearch
import dup
import util

def make_table(pairs):
    result1 = sort.merge_pairs(pairs)                       #merge sort all the pairs, the dupes function only work on sorted files
    result2 = dup.count_dupes_per_file(result1)             #count the number of duplicates for each word in the file
    result3 = dup.merge_dupes_file(result2)                 #make the list for each word to tell in which files it occurs
    for i in range(0,len(result3)):                         #make the list created in previous step descending for all the words
            result3[i][1] = sort.bubbledes(result3[i][1])
    return result3                                          #give output of the table created
