#given a collection of strings of equal length
#return concensus string and matrix
import argparse
import os
#cmd line parser
parser = argparse.ArgumentParser(description='Enter input strings')
parser.add_argument('-f', type=str)
args = parser.parse_args()

if os.path.exists(args.f):
    file = open(args.f,'r')
else:
    print("Please enter a valid path")
    exit()

#TODO proper fasta reader, account for multiline
#---------------------------------------------------------------------------------------------------
names = []
s = []
counter = -1
newseq = False
for line in file:
    if(line[0] == '>'):
        names.append(line.strip()[1::1])
        counter += 1
        newseq = True
    else:
        if newseq:
            s.append(line.strip())
            newseq = False
        else:
            s[counter] += line.strip()
#---------------------------------------------------------------------------------------------------
#make array of strings

#print(s)

#iterate array and count positions
a=[]
c=[]
g=[]
t=[]
for pos in s[1]:
    a.append(0)
    c.append(0)
    g.append(0)
    t.append(0)
i=0
for entry in s:
    while(i < len(entry)):
        if(entry[i] == "A"):
            a[i]+=1
        if(entry[i] == "C"):
            c[i]+=1    
        if(entry[i] == "G"):
            g[i]+=1
        if(entry[i] == "T"):
            t[i]+=1

        i+=1

    i=0    

#go through counts and take highest
s=[]
l=0
while l < len(a):
    max = a[l]
    letter = "A"
    if(c[l] > max):
        max = c[l]
        letter = "C"
    if(g[l] > max):
        max = g[l]
        letter = "G"
    if(t[l] > max):
        max = t[l]
        letter = "T"
    s.append(letter)
    l+=1
#output
i = 0
for entry in s:
    print(entry, end = "")
print()
print("A: ", end = "")
for entry in a:
    print(entry, end = " ")
print()
print("C: ", end = "")
for entry in c:
    print(entry, end = " ")
print()
print("G: ", end = "")
for entry in g:
    print(entry, end = " ")
print()
print("T: ", end = "")
for entry in t:
    print(entry, end = " ")
print()