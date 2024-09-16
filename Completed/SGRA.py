#given a list of numbers L
#return the longest protein string from spectral graph
#---------------------------------------------------------------------------------------------------
#make a directed spectral graph 
#find longest path in spectral graph
#---------------------------------------------------------------------------------------------------
import networkx as nx
import matplotlib.pyplot as plt
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

def find_closest_value_distance(dictionary, target):
    closest_key = min(dictionary, key=lambda k: abs(dictionary[k] - target))
    return abs(dictionary.get(closest_key) - target)

#---------------------------------------------------------------------------------------------------
graph = nx.DiGraph()
for l in L:
    graph.add_node(l)
for current_node in graph.nodes:
    for other_node in graph.nodes:
        diff = current_node - other_node
        #print(diff)
        if find_closest_value_distance(monoisotopic, diff) < 0.001:
            graph.add_edge(current_node, other_node, aa=find_closest_value(monoisotopic, diff))
        #if diff in mono -> add edge between these nodes
#---------------------------------------------------------------------------------------------------
#find longest path
lp = nx.dag_longest_path(graph)
print(lp)
protein_string = []
for i in range(len(lp) - 1):
    start_node = lp[i]
    end_node = lp[i + 1]
    aa = graph[start_node][end_node]['aa']
    protein_string.append(aa)
protein_string.reverse()
a = ''.join(protein_string)
print(a)
#---------------------------------------------------------------------------------------------------
#Visualize
pos = nx.spring_layout(graph)
edge_labels = nx.get_edge_attributes(graph, 'aa')
nx.draw_networkx_edges(graph, pos, width=2, edge_color='gray')
nx.draw_networkx_edge_labels(graph, pos, edge_labels=edge_labels)
nx.draw_networkx(graph, pos, arrows=True, with_labels=True, node_color='red', node_size=300, font_size=10, font_weight='bold')
plt.axis('off')
plt.show()
#---------------------------------------------------------------------------------------------------