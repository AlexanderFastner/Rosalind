#Maximum Matchings and RNA Secondary Structures3
#Given: An RNA string s of length at most 100.
#Return: The total possible number of maximum matchings of basepair edges in the bonding graph of s
#---------------------------------------------------------------------------------------------------
import math
#---------------------------------------------------------------------------------------------------
s= "CGACAUCACCGAUGCCGAUCCUUCUGAUAAGAUACGUGAGGCGUAGCGGAGCACCUUCAGUCAAUGUCCACCCAGCUUGAUCCUUUGUAUUUCAUAGCA"

A = C = G = U = 0
for letter in s:
    match letter:
        case "A":
            A+=1
        case "C":
            C+=1
        case "G":
            G+=1
        case "U":
            U+=1

print("A:", A)
print("C:", C)
print("G:", G)
print("U:", U)
#---------------------------------------------------------------------------------------------------
#Only the maximum matchings count! similar to previous one just need to take min, max of them

permutAU = math.perm(max(A, U), min(A, U))
permutCG = math.perm(max(C, G), min(C, G))

print("permutAU:", permutAU)
print("permutCG:", permutCG)

print(permutAU * permutCG)
#---------------------------------------------------------------------------------------------------