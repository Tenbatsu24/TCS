import ordsearch
import sort
import dup
import util

hacktest = util.words("hacktest.txt")
hacktest = sort.merge(hacktest)
unihacktest = dup.remove_dup(hacktest)
print("unique elements in sorted hacktest.txt: ",len(unihacktest))

print()

grail = util.words("grail.txt")
grail = sort.merge(grail)
unigrail = dup.remove_dup(grail)
print("unique elements in sorted grail.txt: ",len(unigrail))

print()

hacktest = util.words("hacktest.txt")
notunihacktest = dup.remove_dup(hacktest)
print("unique elements in unsorted hacktest.txt: ",len(notunihacktest))

print()

grail = util.words("grail.txt")
notunigrail = dup.remove_dup(grail)
print("unique elements in unsorted grail.txt: ",len(notunigrail))
