#Generate overlap Graph
#O^k with k = userinput. 
#add edge if last k letters in word s match first k letters in t.

#read in all individual headers + respective strings
#for each string compare last k letters with first k letters in nevery other string.
    #if match print both headers
#done
#---------------------------------------------------------------------------------------------------

import argparse
import os

#cmd line parser
parser = argparse.ArgumentParser(description='Enter Fasta File and k')
parser.add_argument('-f', type=str)
parser.add_argument('-k', type=int)
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
k = args.k
for i, n in enumerate(names) :
    end = dna[i][len(dna[i])-3:]
    #print(end)
    for j, other in enumerate(names): 
        start = dna[j][:k]
        #print(start)
        if(i != j):
            if(start == end):
                print(n + " " + other)

