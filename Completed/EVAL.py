#given a positive int n
#a dna string s of even length < 10 
#an array (A) of floats < 20
#return an array B with B having len == A
#B has floats for the probabilities of getting s in a random string t of length n with t having gc content Ai
#---------------------------------------------------------------------------------------------------
import math
#---------------------------------------------------------------------------------------------------
#read inputs
file = open("./rosalind_eval.txt",'r')
a = []
for i, line in enumerate(file):
    if i == 0:
        n = float(line.strip('\n'))
    if i == 1:
        s = line.strip('\n')
    if i == 2:
        l = line.strip('\n').split(" ")
        for e in l:
            a.append(float(e))

print("n: ", n)
print("s: ", s)
print("a: ", a)
print()
#---------------------------------------------------------------------------------------------------
b = []
out = []
for entry in a:
    #entry is GC content %
    GC = entry
    AT = (1-entry)
    # print("GC: ", GC)
    # print("AT: ", AT)

    #letter by letter in s get probability of the occuring in order
    prob = 1
    for l in s:
        if l == 'A' or l == 'T':
            prob *= (AT/2)
        else:
            prob *= (GC/2)
    
    out.append((n- float(len(s)) + 1.0) * prob)
    
def round_half_up(n, decimals=0):
    multiplier = 10 ** decimals
    return math.floor(n * multiplier + 0.5) / multiplier

for o in out:
    #print(o)
    print(round_half_up(o, 3), end=" ")
    
print()
#---------------------------------------------------------------------------------------------------