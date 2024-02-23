#Given: A DNA string s of length at most 100 bp
# and an array A containing at most 20 numbers between 0 and 1.

#Return: An array B
# having the same length as A in which B[k] represents the common logarithm of the probability that a random string constructed with the GC-content found in A[k] will match sexactly.
# python3 PROB.py -s ACGATACAA -A 0.129 0.287 0.423 0.476 0.641 0.742 0.783
#---------------------------------------------------------------------------------------------------
import argparse
import math
import numpy
#---------------------------------------------------------------------------------------------------
parser = argparse.ArgumentParser(description='Enter string s, and array A')
parser.add_argument('-s', type=str)
parser.add_argument('-A', nargs='+', type=float)
args = parser.parse_args()

s = args.s
A = args.A

print("s: ", s)
print("A: ", A)

print()
#---------------------------------------------------------------------------------------------------
#return B so each elem in B is the log of the probability of s matches a random string made with the GC content of A exactly
#x = GC content
#G,C = x/2
#A,T + 1-x/2

B= numpy.zeros(len(A))
i=0

while i < len(A):
    gc = A[i]
    prob = []
    for letter in s:
        if letter == "A" or letter == "T":
            prob.append(math.log10((1-gc)/2))
        else:
            prob.append(math.log10(gc/2))

    B[i] = round(sum(prob),3)
    i+=1

print(B)
