#given n strings of length < 1k
#return the distance matrix
#---------------------------------------------------------------------------------------------------
file = open("./rosalind_pdst.txt",'r')
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
# print("dna: ", dna)
# print()
#---------------------------------------------------------------------------------------------------
def pdist(seq1, seq2):
    length = len(seq1)
    missmatch = 0
    for l1, l2 in zip(seq1, seq2):
        if l1 != l2:
            missmatch+=1
    diff = "%.5f" % (missmatch/length)
    return diff
#---------------------------------------------------------------------------------------------------
def print_matrix(matrix):
    for line in matrix:
        print(*line, sep=" ")
#---------------------------------------------------------------------------------------------------
matrix = []
for s1 in dna:
    new_array = []
    for s2 in dna:
        if s1 == s2:
            new_array.append("%.5f" % 0.00000)
        else:
            new_array.append(pdist(s1, s2))
    matrix.append(new_array)

print_matrix(matrix)
#---------------------------------------------------------------------------------------------------