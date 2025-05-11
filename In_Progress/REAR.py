#given 5 pairs of permutations length 10
#return the reversal distance between them 
#---------------------------------------------------------------------------------------------------

#---------------------------------------------------------------------------------------------------
with open ("./rosalind_rear.txt", 'r') as inputs:
    first = None
    collection = []
    for line in inputs:
        if len(line) > 1:
            if first is not None:
                second = line.strip('\n').split()
                collection.append([first, second])
                first = None
                continue
            else:
                first = line.strip('\n').split()
        
for c in collection:
    print(c)
print('---')
#---------------------------------------------------------------------------------------------------
def swap(pos1, pos2, arr):
    temp=arr[pos1]
    arr[pos1]=arr[pos2]
    arr[pos2]=temp
    return arr

def get_matching(c1, c2):
    matching = [0] * len(c1)
    for i, (j, k) in enumerate(zip(c1, c2)):
        # print(j)
        # print(k)
        if j == k:
            #print('Match at: ', i)
            matching[i] = 1
    return matching

def is_finished(matching):
    for index in matching:
        if index != 1:
            return False
    return True
        

def get_reversal_dist(collection):
    c1, c2 = collection
    swap_counter = 0
    
    print("c1: ", c1)
    print("c2: ", c2)
    print('---')

    #find matches that dont need swapping
    m = get_matching(c1, c2)
    finished = is_finished(m)
    i = 0
    to_swap = None
    print("old macthing: ", m)

    while not finished:
        while i < len(m):
            if m[i] == 1:
                i+=1
            else:
                if to_swap is not None:
                    print("try ", to_swap, i) 
                    #if the swap would work do it
                    if c1[i] == c2[to_swap]:
                        print(c2)   
                        c2 = swap(to_swap, i, c2)
                        print(c2) 
                        m = get_matching(c1, c2)
                        to_swap = None
                        swap_counter +=1
                        print("new macthing: ", m)
                        i = 0
                    else:
                        i+=1
                        continue
                else:
                    print("set to_swap")    
                    to_swap = i
                    i+=1
                    
        finished = is_finished(m)

    return swap_counter

#---------------------------------------------------------------------------------------------------

ans = []
for c in collection:
    ans.append(get_reversal_dist(c))

if len(ans) != 1:
    print(" ".join(str(ans)))


#TODO THIS WORKS but not for the minimum number of swaps