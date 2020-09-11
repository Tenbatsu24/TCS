import sort
import ordsearch
import dup
import util

def word_pairs(filenames):
	"""Return list of word + filename tuples from multiple files"""
	# list to collect resulting pairs
	result = []
	# go over all filenames
	for f in filenames:
		# go over all words in f
		for w in util.words(f):
			# add word+filename pair to result
			result.append([w,f])
	return result

files = ["demo.txt", "hello.txt", "wow.txt"]
lol = word_pairs(files)

def count_files_words(pairs):
        ref = []
        fileindex = 0
        fresh = pairs[0]
        ref.append([fresh[1], 1])
        for i in range(0,len(pairs)):
                if pairs[i][1] == fresh[1]:
                        ref[fileindex][1] += 1
                else:
                        fileindex += 1
                        fresh = pairs[i]
                        ref.append([fresh[1], 1])
        return ref

def calculate_density(pairs, ref):
        for i in range(0,len(pairs)):
                found = False
                j = 0
                value = 1
                while not(found) and j<len(ref):
                        if pairs[i][0] == ref[j][0]:
                                found = True
                                value = ref[j][1]
                        else:
                                j += 1
                pairs[i][1] = round((pairs[i][1]/value),3)
        return pairs

def make_des(result):
    for i in range(0,len(result)):
            result[i][1] = sort.bubbledes(result[i][1])
    return result

def make_table(pairs):
    print("all: ", pairs)
    print()
    ref = count_files_words(pairs)
    print("words in each file: ", ref)
    print()
    result1 = sort.merge_pairs(pairs)
    print("sorted: ", result1)
    print()
    result0 = dup.count_dupes_per_file(result1)
    print("counting dupes: ", result0)
    print()
##    result2 = dup.remove_dup(result1)
##    print("no in file dup: ", result2)
##    print()
    result3 = dup.merge_dupes_file(result0)
    print("merged dupes interfile: ", result3)
    print()
    for i in range(0,len(result3)):
            result3[i][1] = calculate_density(result3[i][1], ref)
    result3 = make_des(result3)
    return result3

table = make_table(lol)
print("des:", table)
