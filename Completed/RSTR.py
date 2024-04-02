#Given: A positive integer N≤100000 , a number x between 0 and 1, and a DNA string s of length at most 10 bp.
#Return: The probability that if N random DNA strings having the same length as s are constructed with GC-content x 
#(see “Introduction to Random Strings”), then at least one of the strings equals s. We allow for the same random 
#string to be created more than once.
#---------------------------------------------------------------------------------------------------
import math
#---------------------------------------------------------------------------------------------------
def calculate_probability(N, x, s):
    # Probability of matching a specific base
    prob_gc = x / 2  # Probability for G or C
    prob_at = (1 - x) / 2  # Probability for A or T

    # Probability of s
    # in example do 0.2 * 0.2 * 0.3...=probability s
    prob_s = 1
    for base in s:
        if base in 'GC':
            prob_s *= prob_gc
        elif base in 'AT':
            prob_s *= prob_at

    # Probability that s is not constructed in one trial
    prob_not_s = 1 - prob_s

    # Probability that s is not constructed in N trials
    prob_not_s_N = prob_not_s ** N

    # Probability that s is constructed at least once in N trials
    prob_at_least_one_s = 1 - prob_not_s_N

    return prob_at_least_one_s
#---------------------------------------------------------------------------------------------------
n = 90981
x = 0.531846
s = 'GTCGAACGAT'
probability = calculate_probability(n, x, s)
print(f"probability: {probability}")







#---------------------------------------------------------------------------------------------------
