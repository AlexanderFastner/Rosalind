#Longest common substring LCSM
#input fasta file
#output the longest common substring

#read input
#---------------------------------------------------------------------------------------------------
import argparse
#---------------------------------------------------------------------------------------------------
#cmd line parser
parser = argparse.ArgumentParser(description='Enter Fasta File')
parser.add_argument('-f', type=str)
args = parser.parse_args()
f = args.f
sequences=[]
current_sequence=""

#read fasta
with open(f, "r") as input:
    for line in input:
        if line.startswith(">"):
            if current_sequence:
                sequences.append(current_sequence)
                current_sequence = ""
        else:
            current_sequence += line.strip()
    
    if current_sequence:  # To handle the last sequence in the file
        sequences.append(current_sequence)
inputs = [line for line in sequences]
print(inputs)
#---------------------------------------------------------------------------------------------------
def printdp(dp):
    for i in dp:
        print(i)

def LCSM(strings):
    def lcs_suffix(s1, s2):
        if isinstance(s1, set) or isinstance(s1, list):
            s1 = list(s1)[0]
        print("s1: ", s1)
        print("s2: ", s2)
        m, n = len(s1), len(s2)
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        length, end_pos = 0, 0
        result_set=[]
        longest_substring=[]
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if s1[i - 1] == s2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                    if dp[i][j] == length:
                        longest_substring.append((i,j))
                    if dp[i][j] > length:
                        longest_substring = [(i,j)]
                        length = dp[i][j]
                        end_pos = i
                else:
                    dp[i][j] = 0
        #printdp(dp)
        #print("end_pos ", end_pos)
        #print("length", length)
        print(longest_substring)
        print()

        if len(longest_substring) == 1:
            #print("Only ONE: ", s1[end_pos - length: end_pos])
            return [s1[end_pos - length: end_pos]]
        #if multiple are found
        else:
            for e in longest_substring:
                result_set.append(s1[e[0] - length: e[0]])
            #print("result_set", result_set)
            return result_set

    # Initialize the LCS as the first string
    common_substring = {strings[0]}
    candidates=[]

    # Compare the current LCS with each string and update it
    #this need to compare every longest substring if there is a tie to decide which to continue with
    for s in strings[1:]:
        print()
        #print("s: ", s)
        print("common substring: ", common_substring)
        
        if not common_substring:
            break  # Early termination

        #common substring a set that always gets smaller as it is limited
        if len(common_substring) != 1:
            print("Multiple substrings in consideration: ", common_substring)
            for i in list(common_substring):
                print("i ", i)
                #add to dict, only keep those with max length
                group = lcs_suffix(i, s)
                candidates.append(group)
                print("candidates", candidates)
            #Only add results with length >= max
            all_strings = [string for sublist in candidates for string in sublist]
            #print("all_strings ", all_strings)
            max_length = max(len(string) for string in all_strings)
            common_substring = {string for string in all_strings if len(string) == max_length}
            candidates = []
            print("common_substring",common_substring)

        #this should only run the first time
        else:
            #print("check1")
            common_substring = lcs_suffix(common_substring, s)
            candidates.append(common_substring)
            #print("check2")
        
    return common_substring
#---------------------------------------------------------------------------------------------------
result = LCSM(inputs)
print(result)