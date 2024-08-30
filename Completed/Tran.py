#given  2 stings calcultae the transition/transversion ratio
#---------------------------------------------------------------------------------------------------
file = open("./rosalind_tran.txt",'r')
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
s1 = dna[0]
s2 = dna[1]

transitions = 0
transversions = 0

for l1, l2 in zip(s1, s2):
    #logic to differntiate transitions and transversions
    #transitions
    #A-T or C-T
    
    if l1 == l2:
        continue
    if l1 == "A" and l2 == "G" or l1 == "G" and l2 == "A":
        transitions+=1
        continue
    if l1 == "C" and l2 == "T" or l1 == "T" and l2 == "C":
        transitions+=1
        continue
    #transversions
    #print("transversion")
    transversions+=1

print("transitions: ", transitions)
print("transversions: ", transversions)
print(transitions/transversions)
#---------------------------------------------------------------------------------------------------