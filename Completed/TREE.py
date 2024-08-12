#input: n= number of nodes, and l adjacency list of those nodes (edges)
#output: min num of edges to make a tree
#---------------------------------------------------------------------------------------------------
with open ("./rosalind_tree.txt", 'r') as inputs:
    n = int(inputs.readline().split()[0])
    lines = inputs.readlines()
    i=0
    found=False
    cycles=[]
    for line in lines:
        tup = set(line.split())
        print("tup: ", tup)
        print("cycles:", cycles)
        print()

        #check set for overlap with each entry in a list of existing sets
        for cycle in cycles:
            print("cycle:", cycle)
            if len(tup.union(cycle)) < len(tup) + len(cycle):
                print("Overlap: ", tup, " ", cycle)
                print()
                cycle.update(tup)
                found=True
                break
            else:
                found=False

        #if no overlap, add new cycle to cycles
        if not found:
            print("Add new cycle: ", tup)
            print()
            cycles.append(tup)
            found=False

#check overlap between all cycle in cycles
def combine_overlapping_sets(set_list):
    changes = True
    while changes:
        changes = False
        for i in range(len(set_list)):
            for j in range(i + 1, len(set_list)):
                if not set_list[i].isdisjoint(set_list[j]):
                    set_list[i] |= set_list[j]
                    set_list.pop(j)
                    changes = True
                    break
            if changes:
                break
    return set_list

#TODO count distinct cycles
#TODO count total number of instances in all sets
#output=distinct_cycles - 1 + (n-in_set)


sets = combine_overlapping_sets(cycles)
tot = 0
for s in sets:
    tot+=len(s)
distinct_cycles = len(sets)


print("n: ", n)
print("sets:", sets)
print()
print("n-total: ", n-tot)
print("output")
print(distinct_cycles - 1 + (n-tot))
print()

#---------------------------------------------------------------------------------------------------