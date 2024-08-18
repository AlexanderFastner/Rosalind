#given two dna strings s and t
#return the collection of indicies where that appears
#only needs to be 1 possibility
#---------------------------------------------------------------------------------------------------
file = open("./rosalind_sseq.txt",'r')
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
s = dna[0]
t = dna[1]
pointer = 0
collection = []

for i, l in enumerate(s):
    if pointer == len(t):
        break
    if l == t[pointer]:
        pointer+=1
        #Rosalind wants 1 indexed
        collection.append(i+1)

for i in collection:
    print(i, end=" ")
print()
#---------------------------------------------------------------------------------------------------