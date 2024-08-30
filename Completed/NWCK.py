#Given a collection of Trees in Newick format
#and a pair of nodes
#Return a collection of integers representing the distance between the given 2 nodes in each tree
#---------------------------------------------------------------------------------------------------
#read inputs into lists
#for both lists at [i] 
    #add distance to each node
    #count distances between
    #write in answer [i]
#---------------------------------------------------------------------------------------------------
from Bio import Phylo
import io
#---------------------------------------------------------------------------------------------------
Trees = []
NodePairs = []
Answers = []

file = open('./rosalind_nwck.txt', 'r')
for i, line in enumerate(file):
    line = line.strip()
    if len(line) < 1:
        continue
    if line.startswith("("):
        Trees.append(line)
    else:
        NodePairs.append(line)
        
# print(Trees)
# print(NodePairs)
# print()
# print()
#---------------------------------------------------------------------------------------------------
for i in zip(Trees,NodePairs):
    t, search = i
    first_node, second_node = search.split(" ")
    tree = Phylo.read(io.StringIO(t),'newick')
    clades = tree.find_clades()
    for clade in clades:
        clade.branch_length = 1
    Answers.append(tree.distance(first_node, second_node))
    # print(tree)
    # print(clades)
for j in Answers:
    print(j, end=" ")
print()
#---------------------------------------------------------------------------------------------------