#Given: Two positive integers k(k≤7) and N(N≤2k). 
#In this problem, we begin with Tom, who in the 0th generation has genotype Aa Bb. 
#Tom has two children in the 1st generation, each of whom has two children, and so on. 
#Each organism always mates with an organism having genotype Aa Bb.

#Return: The probability that at least N Aa Bb organisms will belong to the k-th generation of Tom's family tree 
#(don't count the Aa Bb mates at each level). Assume that Mendel's second law holds for the factors.

#Inputs
k = 5 #k-th  generation (generations are a binary tree)
N = 8 #N number of individuals

##########

#Idea
#for each individual starting from N all the way down the tree
    #add their probability to sum for all
        #calculate by binomial coefficent * probability of AaBb * (P(not AaBb) ** (everyone else)) 
            #This is because they arent independent, and the probability of a 3 gen individual being AaBb is affected by the generation above

def binomial_coefficient(n, k):
    if k < 0 or k > n:
        return 0
    if k == 0 or k == n:
        return 1
    k = min(k, n - k)
    c = 1
    for i in range(k):
        c = c * (n - i) // (i + 1)
    return c

def probability_of_AaBb(k, N):
    total_offspring = 2 ** k
    #Starting genotype
    prob_AaBb = 0.25  
    prob_at_least_N = 0

    for i in range(N, total_offspring + 1):
        prob_at_least_N += binomial_coefficient(total_offspring, i) * (prob_AaBb ** i) * ((1 - prob_AaBb) ** (total_offspring - i))

    return round(prob_at_least_N, 3)

#output
print(probability_of_AaBb(k, N))