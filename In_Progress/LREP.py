#Finding the longest multiple repeat
#---------------------------------------------------------------------------------------------------
#input: A DNA string s with $ appended, a positive int k and a list of edges defining a suffix tree s
#return the longest substring of s that occuirs at leeast k times in s. (return any solution)
#---------------------------------------------------------------------------------------------------
import networkx as nx
#---------------------------------------------------------------------------------------------------
with open ("./rosalind_lrep.txt", 'r') as inputs:
    edges = []
    for i, line in enumerate(inputs):
        if len(line) > 1:
            match i:
                case 0:
                    s = line.strip('\n')
                case 1:
                    k = line.strip('\n')
                case _:
                    edges.append(line.strip('\n').split())

#Test inputs
print("s: ", s)
print("k: ", k)
print('---')
for c in edges:
    print(c)
print('---')
#---------------------------------------------------------------------------------------------------
#THE INTERNAL NODES ARE THE SUBSTRINGS
#COUNT THE NUMBER OF LEAF NODES DOWN FROM EACH BRANCH


#if start pos and length are the same-its the same substring
    #make groups of edges that are the same substring
#track 
for edge in edges:
    if edge[3] < k:
        continue
    else:
        print("candidate")
        print(edge)

#---------------------------------------------------------------------------------------------------
