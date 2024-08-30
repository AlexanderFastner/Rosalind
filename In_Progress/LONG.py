#given 50 strings of length < 1000 that overlap by >50% make a superstring
#---------------------------------------------------------------------------------------------------
#Naive
#read all strings from fasta format
#loop through all options and look for overlap >50%
    #fuse
    #repeat
#done :)
#---------------------------------------------------------------------------------------------------
file = open("./rosalind_long.txt",'r')
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
#function to loop through a list and get the first entry with a 50% overlap
#return both the new fused and the shortened dna list
def get_overlap(s, l):
    if s in "":
        return l[0], l[1:]

    #if first 50% is a substring of fused it is added
    for read in l:
        print("start: ", read)
        print("fused: ", s)
        print()
        max_overlap = min(len(s), len(read))
        for i in range(max_overlap, 0, -1):
            if s.endswith(read[:i]):
                return s + read[i:]
            
    #if last 50% is a substring of fused it is added
    for read in l:
        print("end: ", read)
        print("fused: ", s)
        print()
        max_overlap = min(len(read), len(s))
        for i in range(max_overlap, 0, -1):
            if read.endswith(s[:i]):
                return read + s[i:]

#---------------------------------------------------------------------------------------------------

print("dna: ", dna)
print()
fused = ""
finished = False
while not finished:
    fused, dna = get_overlap(fused, dna)
    print("fused: ", fused)
    print("dna: ", dna)
    print()
#finished = True

#---------------------------------------------------------------------------------------------------
