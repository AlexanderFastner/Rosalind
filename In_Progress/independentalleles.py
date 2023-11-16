#independent alleles
#given k, n : n < 2^k
#0th generation is AaBb
#always two children
#each child reproduces with AaBb
#return probability of at least n AaBb in kth generation (dont count the added AaBb mates)
import math

k = 2
n = 1

#1st gen
#AABB 1/16
#AABb 2/16
#AAbb 1/16
#AaBB 2/16
#AaBb 4/16
#Aabb 2/16
#aaBB 1/16
#aaBb 2/16
#aabb 1/16

#chance of making AaBb offpring
#AABB 1/16
#AABb 2/16
#AAbb 1/16
#AaBB 2/16
#AaBb 4/16
#Aabb 2/16
#aaBB 1/16
#aaBb 2/16
#aabb 1/16

parents = (k-1)**2
children = k**2

#probability of at least n children with AaBB of a given number of parents = 1 - probability of at most n-1 children
#P(children with AaBb < n-1) =  sum 0 to n  (parents choose n-1) * (liklyhoods of AaBb)^n * (liklyhood of not AaBb)^parents-n-1
#sum 0 to n is a loop of this eqation !!!!!!!!!!!!!!!!
probability = (math.comb(parents, (children-1))) * (.25)**(n-1) * (.75)**(parents-n-1)

print(probability)

