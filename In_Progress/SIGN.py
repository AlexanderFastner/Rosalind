#create all permutations of signed integers of length n
#---------------------------------------------------------------------------------------------------
import itertools
import numpy as np
#---------------------------------------------------------------------------------------------------
n=3
#---------------------------------------------------------------------------------------------------
#create all permutations counting the sign as differing 

total=0
input_array= np.arange(1,n+1,1).tolist()
#all positive permutations
x=list(itertools.permutations(input_array))
print(x)
#now iterate through all permutations with negatives
for arrangement in x:
    #permute (+/-) through all of them
    print(arrangement)
    

#total number of permutations
#print()
#permutaions in any order
#print()
#---------------------------------------------------------------------------------------------------