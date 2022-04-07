#take rna string and give back AA sequence
import argparse
import os
#cmd line parser
parser = argparse.ArgumentParser(description='Enter input strings')
parser.add_argument('-s', type=str)
args = parser.parse_args()
s = args.s
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


#check len divisible by 3
if len(s)%3 != 0:
    print("Sequence not divisible by 3!")

i = 0
while i < len(s):
    if s[i:i+3] in protDict:
        if protDict[s[i:i+3]] == "Stop":
            print("", end = "")
        else:
            print(protDict[s[i:i+3]], end = "")
        i+=3     
    else:
        print("error seq not recognized")
print()