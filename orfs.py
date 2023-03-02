# given a DNA strinng s 
# return all possible orfs
import argparse
import os
from pickle import TRUE
#cmd line parser
parser = argparse.ArgumentParser(description='Enter input strings')
parser.add_argument('-s', type=str)
args = parser.parse_args()
s = args.s

#get reverse complement
out = ""
for letter in s:
    if letter == "A":
        out += "T"
    if letter == "C":
        out += "G"
    if letter == "G":
        out += "C"
    if letter == "T":
        out += "A"
i = len(out) - 1
res = ""
while i >= 0:
    res+=(out[i])
    i -= 1

s1 = res

#get RNA
out = ""
for letter in s:
    if letter == 'T':
        out += 'U'
    else:
        out += letter
prot=out
out = ""
for letter in s1:
    if letter == 'T':
        out += 'U'
    else:
        out += letter
prot1=out

#print(prot)
#print(prot1)

#prot dict
protDict = {
"UUU":"F", "CUU":"L", "AUU":"I", "GUU":"V",
"UUC":"F", "CUC":"L", "AUC":"I", "GUC":"V",
"UUA":"L", "CUA":"L", "AUA":"I", "GUA":"V",
"UUG":"L", "CUG":"L", "AUG":"M", "GUG":"V",
"UCU":"S", "CCU":"P", "ACU":"T", "GCU":"A",
"UCC":"S", "CCC":"P", "ACC":"T", "GCC":"A",
"UCA":"S", "CCA":"P", "ACA":"T", "GCA":"A",
"UCG":"S", "CCG":"P", "ACG":"T", "GCG":"A",
"UAU":"Y", "CAU":"H", "AAU":"N", "GAU":"D",
"UAC":"Y", "CAC":"H", "AAC":"N", "GAC":"D",
"UAA":"*", "CAA":"Q", "AAA":"K", "GAA":"E",
"UAG":"*", "CAG":"Q", "AAG":"K", "GAG":"E",
"UGU":"C", "CGU":"R", "AGU":"S", "GGU":"G",
"UGC":"C", "CGC":"R", "AGC":"S", "GGC":"G",
"UGA":"*", "CGA":"R", "AGA":"R", "GGA":"G",
"UGG":"W", "CGG":"R", "AGG":"R", "GGG":"G",
}

temp= ""
output = []
#TODO if not divisible by 3 then shift start of orf by extra

#check len divisible by 3
if len(prot)%3 != 0 or len(prot1)%3 != 0:
    print("Warning Sequence not divisible by 3!")

#TODO 
#cut last letter, but also start translating from 1/2 letters in 

#translate to list of all 6 orf AA sequences
def rna2prot(seq, rev):
    o = []
    #seq, and rev 3 times each with varied start
    for j in range(3):
        AAs = ""
        AAr = ""
        i = len(seq)%3
        #print(j)
        #print(i)
        #print("seq" + seq)
        #print("rev" + rev)
        #print(len(seq))
        while i+3 <= len(seq):
            AAs += protDict[seq[i:i+3]]
            AAr += protDict[rev[i:i+3]]
            i += 3
        #print(AAs)
        o.append(AAs)
        o.append(AAr)
        seq = seq[:-1]
        rev = rev[:-1]
    return o

#print(prot)
#print(prot1)
rnaprot = rna2prot(prot, prot1)
#print(rnaprot)

#for each orf get M-* for each M-* combination, if not * then not a combination 

def orf_iter(seq):
    s = ""
    start = False
    #loop through seq
    #print(seq)
    l = 0
    while l < len(seq):
        #if M found start
        if not start:
            if seq[l] == "M":
                start = True
                s += "M"
                l += 1
                prev = l
            else :
                l += 1
        else:
            if seq[l] == "*":
                output.append(s)
                s = ""
                start = False
                l = prev
            else:
                s += seq[l]
                l += 1

#for each AA seq check for possible proteins
for var in rnaprot:
    orf_iter(var)
#remove dups from output
output = list(set(output))
#print(output)

for i in output:
    print(i)