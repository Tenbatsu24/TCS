import sort
import ordsearch
import dup

def make_table(pairs):
    result1 = sort.merge_pairs(pairs)           #merge sort all the pairs
    result2 = dup.remove_dup(result1)           #removes the duplicates in the word pairs
    result3 = dup.merge_dupes_file(result2)     #same words having different file names are put into one list as specification asks
    return result3
