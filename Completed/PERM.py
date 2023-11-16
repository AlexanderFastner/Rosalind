#Given: A positive integer n≤7
#Return: The total number of permutations of length n, followed by a list of all such permutations (in any order).
import math
import itertools

n = 7
total = math.factorial(n)

#make base list of 1-n
base = []
i = 0
while i < n:
    i = i + 1
    base.append(i)
#print(base)

#shuffle all permutations of base
out = list(itertools.permutations(base))

#output
with open("output.txt", "a") as o:
    o.write(str(total) + "\n")
    for i in out:
        for entry in i:
            o.write(str(entry) + " ")
        o.write("\n")