#create all permutations of signed integers of length n
#---------------------------------------------------------------------------------------------------
import itertools
import numpy as np
import math
#---------------------------------------------------------------------------------------------------
n=3
#---------------------------------------------------------------------------------------------------
def generate_permutations(arrangement):
    signs = itertools.product([-1, 1], repeat=len(arrangement))
    permutations = []
    
    for sign_combination in signs:
        permutation = [num * sign for num, sign in zip(arrangement, sign_combination)]
        permutations.append(permutation)
    
    return permutations
#---------------------------------------------------------------------------------------------------
#create all permutations counting the sign as differing 

total=0
input_array= np.arange(1,n+1,1).tolist()
#all positive permutations
x=list(itertools.permutations(input_array))
#print(x)
#TODO total
total = math.perm(n, n) * len(list(itertools.product([-1, 1], repeat=n)))
print(total)
#now iterate through all permutations with negatives
with open('./rosalind_out.txt', 'w') as o:
    o.write(str(total) + "\n")
    for arrangement in x:
        #add (+/-) through all of them
        result = generate_permutations(arrangement)
        for perm in result:
            for item in perm:
                o.write(str(item)+" ")
            o.write('\n')
#---------------------------------------------------------------------------------------------------