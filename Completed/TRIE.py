#given a list of 100 DNA strings len(100)
#return adjacency list of a Trie in following format
#first label the root with 1 
#label the remaining nodes with the integers 2 through nin any order
#Each edge of the adjacency list of T will be encoded by a triple containing the integer representing the edge's parent node, followed by the integer representing the edge's child node, and finally the symbol labeling the edge.
#---------------------------------------------------------------------------------------------------
import networkx as nx
import matplotlib.pyplot as plt
import pydot
from networkx.drawing.nx_pydot import graphviz_layout
#---------------------------------------------------------------------------------------------------
with open ("./rosalind_trie.txt", 'r') as inputs:
    IN= inputs.read().split()
    L= [i for i in IN]
print("L", L)
print()
#---------------------------------------------------------------------------------------------------
#build Trie
def build_trie(L):
    T = nx.DiGraph()
    node_count = 1
    T.add_node(1)

    for word in L:
        current = 1
        for char in word:
            if not any(T.get_edge_data(current, child).get('label') == char 
                       for child in T.successors(current)):
                # If no edge with this char exists, create a new node
                node_count += 1
                T.add_edge(current, node_count, label=char)
                current = node_count
            else:
                # If edge exists, move to the existing node
                current = next(child for child in T.successors(current) 
                               if T.get_edge_data(current, child)['label'] == char)
    
    return T
#---------------------------------------------------------------------------------------------------
#plot Trie pretty :)
def hierarchy_pos(G, root, width=1., vert_gap = 0.2, vert_loc = 0, xcenter = 0.5):
    pos = {root: (xcenter, vert_loc)}
    children = list(G.neighbors(root))
    if not children:
        return pos
    dx = width / len(children) 
    nextx = xcenter - width/2 - dx/2
    for child in children:
        nextx += dx
        pos.update(hierarchy_pos(G, child, width = dx, vert_gap = vert_gap, 
                                 vert_loc = vert_loc-vert_gap, xcenter=nextx))
    return pos
#---------------------------------------------------------------------------------------------------
#Make Trie
T = build_trie(L)

#---------------------------------------------------------------------------------------------------
#output formatting
# for edge in T.edges(data=True):
#     #print(f"Edge: {edge[0]} -> {edge[1]}, Label: {edge[2]['label']}")
#     print(f"{edge[0]} {edge[1]} {edge[2]['label']}")

with open('rosalind_trie_output.txt', 'w') as out:
    for edge in T.edges(data=True):
        out.write(f"{edge[0]} {edge[1]} {edge[2]['label']}\n")

#---------------------------------------------------------------------------------------------------
#Vizualize
# pos = hierarchy_pos(T, root=1)
# nx.draw(T, pos, with_labels=True, node_color='lightblue', 
#         node_size=300, font_size=14, arrows=True)
# elabels = {(u, v): l for u, v, l in T.edges(data="label")}
# nx.draw_networkx_edge_labels(T, pos, edge_labels=elabels)
# plt.title("Trie Visualization")
# plt.axis('off')
# plt.tight_layout()
# plt.show()
#---------------------------------------------------------------------------------------------------