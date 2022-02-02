#find GC content
import argparse
import os

#cmd line parser
parser = argparse.ArgumentParser(description='Enter Fasta File')
parser.add_argument('-f', type=str)
args = parser.parse_args()

#check if path exists
if os.path.exists(args.f):
    file = open(args.f,'r')
else:
    print("Please enter a valid path")
    exit()

#---------------------------------------------------------------------------------------------------
names = []
dna = []
counter = -1
newseq = False
for line in file:
    if(line[0] == '>'):
        names.append(line.strip()[1::1])
        counter += 1
        newseq = True
    else:
        if newseq:
            dna.append(line.strip())
            newseq = False
        else:
            dna[counter] += line.strip()
#---------------------------------------------------------------------------------------------------
#console output        
i = 0
gcContent = 0
totalLen  = 0
while i < len(names):
    print(names[i], end = " ")
    totalLen = len(dna[i])
    for letter in dna[i]:
        if letter == 'C' or letter == 'G':
            gcContent += 1
    print(round((gcContent/totalLen)*100, 6), end = "")
    print('%')
    gcContent = 0
    i += 1