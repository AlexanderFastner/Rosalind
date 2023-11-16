#RNA SPLICING
#input dna sequence
#output spliced only exons as AA sequence

#### IMPORTS
import argparse
import re
import Bio
from Bio import SeqIO
###

#cmd line parser
parser = argparse.ArgumentParser(description='Enter input File')
parser.add_argument('-f', type=str)
args = parser.parse_args()
f = args.f


#read input file
with open(f, "r") as input:
    sequences = [line.strip() for line in input]
input.close()

s = ""
introns = []
first = True
#TODO read in fasta correctly
#s for first sequence
#introns as list of all other sequences
for sequence in SeqIO.parse(f, "fasta"):
    if first:
        s = str(sequence.seq)
        #print(s)
        first = False
    else:
        #print(sequence.seq)
        introns.append(str(sequence.seq))

print("original:  " + s)
#find and remove introns from s
for i in introns:
    s = re.sub(i, "", s)
print("removed introns: " + s)

#get RNA
def get_rna(dna):
    out = dna.replace('T', "U")
    return out

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
#get prot
def rna2prot(seq):
    o = []
    AA = ""
    i = 0
    while i+3 <= len(seq):
        AA += protDict[seq[i:i+3]]
        i += 3
    o.append(AA)
    return o

s = get_rna(s)
print("final : " + s)
s = rna2prot(s)[0]
s = s.split("*")[0]
#try cut from start to M
s = "M" + s.split("M", 1)[1]
print()
print(s)