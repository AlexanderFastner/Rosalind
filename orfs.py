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
"UAA":"Stop", "CAA":"Q", "AAA":"K", "GAA":"E",
"UAG":"Stop", "CAG":"Q", "AAG":"K", "GAG":"E",
"UGU":"C", "CGU":"R", "AGU":"S", "GGU":"G",
"UGC":"C", "CGC":"R", "AGC":"S", "GGC":"G",
"UGA":"Stop", "CGA":"R", "AGA":"R", "GGA":"G",
"UGG":"W", "CGG":"R", "AGG":"R", "GGG":"G",
}

temp= ""
output = []

#check len divisible by 3
if len(prot)%3 != 0 or len(prot1)%3 != 0:
    print("Warning Sequence not divisible by 3!")
    #print(len(prot)%3)


#TODO fix bug when not %3 
#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!


#translate at different starts regular
j = 0
start=False
while j < 3:
    i = j
    while i < len(prot):
        if prot[i:i+3] in protDict:
            if not start:
                if protDict[prot[i:i+3]] == "M":
                    start=True
                    print("START Found", i)
                else:
                    i+=3
            else:
                if protDict[prot[i:i+3]] == "Stop":
                    print("STOP Found", i)
                    start=False
                    output.append(temp)
                    temp=""
                else:
                    temp += protDict[prot[i:i+3]]
                    #print(protDict[prot[i:i+3]], end = "")
                i+=3     
        else:
            print(prot[i:i+3])
            print(i)
            print(len(prot))
            print("error seq not recognized")
    j+=1
    start=False
    output.append(temp)
    temp=""

#translate at different starts reverse
j = 0
while j < 3:
    i = j
    while i < len(prot1):
        if prot1[i:i+3] in protDict:
            if not start:
                if protDict[prot[i:i+3]] == "M":
                    start=True
                else:
                    i+=3
                    continue 
            
            if protDict[prot1[i:i+3]] == "Stop":
                print("", end = "")
                break
            else:
                temp += protDict[prot1[i:i+3]]
                #print(protDict[prot1[i:i+3]], end = "")
            i+=3     
        else:
            print("error seq not recognized")
    j+=1
    output.append(temp)
    temp=""

for entry in output:
    print(entry)