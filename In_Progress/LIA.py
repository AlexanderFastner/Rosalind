#Given: Two positive integers k(k≤7) and N(N≤2k). 
#In this problem, we begin with Tom, who in the 0th generation has genotype Aa Bb. 
#Tom has two children in the 1st generation, each of whom has two children, and so on. 
#Each organism always mates with an organism having genotype Aa Bb.

#Return: The probability that at least N Aa Bb organisms will belong to the k-th generation of Tom's family tree 
#(don't count the Aa Bb mates at each level). Assume that Mendel's second law holds for the factors.

#Aa = 1/2
#AA = 1/4
#aa = 1/4
#Bb = 1/2
#BB = 1/4
#bb = 1/2
#AaBb = P(Aa) * P(Bb) = 1/2 * 1/2 = 1/4
##########

#Inputs
k = 2 #k-th  generation (generations are a binary tree)
N = 1 #N number of individuals
out = 0 #Probability that !!!AT LEAST!!! N individuals are in the k-th generation
##########

#TOM-2-4 = P(AaBb) in 4 = 0.684
#out = P(1/4 = AaBb) + P(2/4 = AaBb) + P(3/4 = AaBb) + P(4/4 = AaBb) or 1- P(0/4 = AaBb)
#out = P(N/k^2 = AaBb) + P(N+1/k^2 = AaBb) + ...
#P(1/4 = AaBb) = 1/4
#P(2/4 = AaBb) = 1/16
#P(0/4 = AaBb) = 3/4 * 3/4 * 3/4 * 3/4

#write so that every probability is checked

#fix, P(1/16 = AaBb != 1/4)
num = 2**k
i = N
tot = 0
while i <= num:
    print(i)
    liklihood = ((1/4)**i)
    print("liklhood:", liklihood)
    i+=1
    tot += liklihood

print("total:", 1- tot)