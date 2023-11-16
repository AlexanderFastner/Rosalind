#Longest common substring LCSM
#input fasta file
#output the longest common substring

#PSEUDO code for 2 strings
# function LCSubstr(S[1..r], T[1..n])
#     L := array(1..r, 1..n)
#     z := 0
#     ret := {}

#     for i := 1..r
#         for j := 1..n
#             if S[i] = T[j]
#                 if i = 1 or j = 1
#                     L[i, j] := 1
#                 else
#                     L[i, j] := L[i − 1, j − 1] + 1
#                 if L[i, j] > z
#                     z := L[i, j]
#                     ret := {S[i − z + 1..i]}
#                 else if L[i, j] = z
#                     ret := ret ∪ {S[i − z + 1..i]}
#             else
#                 L[i, j] := 0
#     return ret


#read input
#---------------------------------------------------------------------------------------------------
import argparse
import os
#---------------------------------------------------------------------------------------------------

#cmd line parser
parser = argparse.ArgumentParser(description='Enter Fasta File')
parser.add_argument('-f', type=str)
args = parser.parse_args()
f = args.f

#read fasta
with open(f, "r") as input:
    sequences = [line.strip() for line in input]
input.close()



