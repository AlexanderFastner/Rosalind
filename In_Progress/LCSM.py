#Longest common substring LCSM
#input fasta file
#output the longest common substring

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

for line in sequences:
    print(line)

#---------------------------------------------------------------------------------------------------



#---------------------------------------------------------------------------------------------------


