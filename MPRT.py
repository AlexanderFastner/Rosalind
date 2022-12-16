#Finding a Protein Motif
#input up to 15 UniProt Ids
#if contains N-glycosylation motif output protein id and (space seperated) locations of this motif 

#### IMPORTS
import argparse
import os
import requests
import re
###

#cmd line parser
parser = argparse.ArgumentParser(description='Enter input File')
parser.add_argument('-f', type=str)
args = parser.parse_args()
f = args.f

#base dir
base_dir = os.getcwd()

#read input file
with open(f, "r") as input:
    #list of proteinids
    protids = [line.strip() for line in input]
input.close()

pattern = "(?=(N[^P][S|T][^P]))"
for line in protids:
    #print(line)
    org = line
    line = line.split(sep = "_")[0]

    url = "http://www.uniprot.org/uniprot/" + line  + ".fasta"
    response = requests.get(url).text
    #print(response)
    sequence = ""
    sequence = ''.join(response.split(sep = "\n")[1:])
    
    #print(sequence)
    #regex match N-glycosylation motif N{P}[ST]{P} against all 
    x = re.findall(pattern, sequence)
    if(len(x)!= 0):
        print(org)

    matches = re.finditer(r'(?=(N[^P][S|T][^P]))', sequence)
    #print([(match.span()[1] + 1) for match in matches])
    results = [(match.span()[1] + 1) for match in matches]
    #results = [match.group(1) for match in matches]
    #print(results)

    for e in results:
        print(e, end = " ")
    print()