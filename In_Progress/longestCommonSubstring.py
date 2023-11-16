#find longest common substring

#read input
#---------------------------------------------------------------------------------------------------
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
#find shortest pattern
shortestLen = float('inf')
shortestSeq = ""
for seq in dna:
    if len(seq) < shortestLen:
        shortestLen = len(seq)
        shortestSeq = seq

print(shortestLen)
print(shortestSeq)
#---------------------------------------------------------------------------------------------------
#split shortestSeq into k-mers list
kmers = []
c = shortestLen
for i in range(c-1, -1, -1):
    #build all i-mers

    for j in range(0, shortestLen +1, 1):
        if j-i -1< 0:
            kmer = shortestSeq[j: j + shortestLen-i]
            if kmer not in kmers:
                #cut out dups
                kmers.append(kmer)   
#sort kmers by len
kmers.sort(key = len, reverse=True)
print(kmers)  
#---------------------------------------------------------------------------------------------------
def findSubstring(k, s):
    #find substrings
    c = 1
    for count, letter in enumerate(s):
        if letter == k[0]:
            if((count + len(k)) <= len(s)):
                #patch
                if len(k) == 1:
                    print("found " + k)
                    return True
                for i in range (count+1, (count + len(k))):
                    if k[c] == s[i]:
                        c+=1
                    else:
                        c = 1
                        break
                    if c == len(k):
                        print("found " + k)
                        return True
print() 
#---------------------------------------------------------------------------------------------------
rm = []
#scan all sequences and eliminate from k-mers list
for s in dna:
    print(s)
    print()
    #pattern match every kmer
    for kmer in kmers:
        #eliminate kmer from list if not found
        if not findSubstring(kmer, s):
            print("kmer not found " + kmer)
            rm.append(kmer)
    for elem in rm:
        if elem in kmers:
            kmers.remove(elem)
    #print(kmers)
for e in kmers:
    print(e, end = ' ')
print()



#---------------------------------------------------------------------------------------------------

