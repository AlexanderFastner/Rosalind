#Given: An RNA string s of length at most 80 bp having the same number of occurrences of 'A' as 'U' and the same number of occurrences of 'C' as 'G'.
#Return: The total possible number of perfect matchings of basepair edges in the bonding graph of s
#---------------------------------------------------------------------------------------------------
import numpy as np
import itertools
from itertools import permutations 
import math
#---------------------------------------------------------------------------------------------------
s = "CGCAGCUGUAGGUCAUAUCCCGUCAAAUUUUGGGCGACACAUGAUUCCGUGAACUGGUCAAUGCCGAAAAUU"
print(len(s))
perfect_matches = 0
#perfect match = set of matches with no node having more than 1 edge 
    #can represent as a set of tuples all of size 2
    #further restricted by only being able to bond A-T and C-G
    #can switch edge between A1-T1 A2-T2, but not between A1-T1 C1-G1


#idea
#array of len n for n=#A in s
    #n must be same for A/T and C/G
#index is useful for keeping unique letters
#permutations to get all possible ways to pick sets of 2 from the 2 lists(x2 for AT, CG)
#---------------------------------------------------------------------------------------------------
AU = 0
CG = 0

for l in s:
    if "A" in l:
        AU+=1
    if "C" in l:
        CG+=1

A_array = ['A'] * AU
C_array = ['C'] * CG

permut = math.perm(len(A_array), len(A_array))
permut1 = math.perm(len(C_array), len(C_array))
print(permut)
print(permut1)
print(permut * permut1)