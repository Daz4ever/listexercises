

listofnum = [-1, -4, 5, 4, 3, 2, 7]

print "Given an list of numbers, print their sum."
print sum(listofnum)

print "Given an list of numbers, print the largest of the numbers."
print max(listofnum)

print "Given an list of numbers, print the smallest of the numbers."
print min(listofnum)

print "Given an list of numbers, print each number in the list that is even."

for i in listofnum:
    if i % 2 == 0:
        print i

print "Given an list of numbers, print each number in the list that is greater than zero."

for i in listofnum:
    if i > 0:
        print i

print """Given an list of numbers, create a new list which contains every number
 in the given list which is positive."""

listofeven = []
for i in listofnum:
    if i % 2 == 0:
        listofeven.append(i)
print listofeven


print """

Given an list of numbers, and a single factor (also a number), create a new list
 consisting of each of the numbers in the first list multiplied by the factor.
 Print this list using console.log(list);

 """
listfactored = []

for i in listofnum:
    listfactored.append(i * 3)
print listfactored

print """Given two lists of numbers of the same length, create a new list by multiplying
the pairs of numbers in corresponding positions in the two lists."""

firstlist = [1, 3, 6, 9]
secondlist = [2, 4, 6, 8]
multipliedlist = []

for i in range(0, len(firstlist)):
    multipliedlist.append(firstlist[i] * secondlist[i])
print multipliedlist

print " "
