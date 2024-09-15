#given a list of numbers L
#return the longest protein string from spectral graph
#---------------------------------------------------------------------------------------------------
#make a directed spectral graph 
#find longest path in spectral graph
#---------------------------------------------------------------------------------------------------
import networkx as nx
#---------------------------------------------------------------------------------------------------
monoisotopic={
"A":71.03711,
"C":103.00919,
"D":115.02694,
"E":129.04259,
"F":147.06841,
"G":57.02146,
"H":137.05891,
"I":113.08406,
"K":128.09496,
"M":131.04049,
"N":114.04293,
"P":97.05276,
"Q":128.05858,
"R":156.10111,
"S":87.03203,
"T":101.04768,
"V":99.06841,
"W":186.07931,
"Y":163.06333,
}
#---------------------------------------------------------------------------------------------------
with open ("./rosalind_sgra.txt", 'r') as inputs:
    IN= inputs.read().split()
    L= [round(float(i), 7) for i in IN]
print("L", L)
print()
#---------------------------------------------------------------------------------------------------
def find_closest_value(dictionary, target):
    closest_key = min(dictionary, key=lambda k: abs(dictionary[k] - target))
    return closest_key
#---------------------------------------------------------------------------------------------------
graph = nx.DiGraph()
for l in L:
    graph.add_node(l)

for current_node in graph.nodes:
    for other_node in graph.nodes:
        diff = current_node - other_node
        print(diff)

        #if diff in mono -> add edge between these nodes