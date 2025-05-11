#Counting Subsets
#Given a positive int n
#Return the toal number of subsets % 1.000.000
#---------------------------------------------------------------------------------------------------
from itertools import combinations
#---------------------------------------------------------------------------------------------------
#Technicaly correct but just using the formula is so much faster
# n = c = 995
# count = 0
# while n > 0:
#     for i in combinations(range(c), n):
#         # print(i)
#         count+=1
#     n = n-1
# count+=1
#---------------------------------------------------------------------------------------------------
count = 2**895
print(count)
print("___")
print(count%1000000)
#---------------------------------------------------------------------------------------------------