#given 50 strings of length < 1000 that overlap by >50% make a superstring
#---------------------------------------------------------------------------------------------------
#Naive
#read all strings from fasta format
#loop through all options and look for overlap >50%
    #fuse
    #repeat
#done :)
#---------------------------------------------------------------------------------------------------
from collections import namedtuple
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
#function to loop through a list and get the overlap
Overlap = namedtuple('Overlap', ['start', 'end', 'length'])

def get_overlap(first, second):
    print("first: ", first)
    print("second: ", second)
    print()
    overlap = None
    max_overlap = len(second)

    for i in range(int(max_overlap/2), max_overlap):
        if first[-i:] == second[:i]:
            print("end match")
            overlap = Overlap(start=first, end=second, length=i)
        elif second[-i:] == first[:i]:
            print("start match")
            overlap = Overlap(start=second, end=first, length=i)
        elif overlap:
            return overlap
        
    return Overlap(start=first, end=second, length=0)
#---------------------------------------------------------------------------------------------------
def combine(overlap):
    return f'{overlap.start}{overlap.end[overlap.length:]}'
#---------------------------------------------------------------------------------------------------


print("dna: ", dna)
print()
fused = dna[0]
dna = dna[1:]
finished = False
while not finished:
    #loop through and find overlap between the fused sequence
    #this will not always return a match -if not keep trying 
    for s in dna:
        o = get_overlap(fused, s)
        print('o ', o)
        print()
        if o.length != 0:
            fused = combine(o)
            print()
            print("fused: ", fused)
            dna.remove(s)
            print("dna after: ", dna)
            print()

    if len(dna) == 0:
            finished = True
#---------------------------------------------------------------------------------------------------