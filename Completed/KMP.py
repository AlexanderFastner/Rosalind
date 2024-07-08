#find the failure array of string s
#---------------------------------------------------------------------------------------------------
#given a string s 
#find the failure array
#the failure array as implemented in Knuth Morris Pratt
#array keeps track of the length of the substring that matches the start of s
#---------------------------------------------------------------------------------------------------
import numpy as np
#---------------------------------------------------------------------------------------------------
with open ("./rosalind_kmp.txt", 'r') as inputs:
    first=inputs.readline()
    s=inputs.read().strip().replace("\n", "")
    print("len(s): ", len(s))
#---------------------------------------------------------------------------------------------------
# this is the same as finding lps
#the longest possible proper prefix which is also a suffix of pattern
#The pattern in this case is s itself
def find_failure_array(s):
    failure_array=np.zeros(len(s), dtype=int)
    prefix=0
    i=1
    while i < len(s):
        # print("failure_array",failure_array)
        # print('i: ', i)
        if s[i] == s[prefix]:
            prefix+=1
            failure_array[i] = prefix
            i+=1
        else:
            if prefix != 0:
                prefix=failure_array[prefix-1]
            else:
                failure_array[i] = 0
                i+=1

    return failure_array
#---------------------------------------------------------------------------------------------------
with open('./answerKMP.txt', 'w') as answer:
    for i in find_failure_array(s):
        answer.write(str(i),)
        answer.write(" ")
answer.close()
#---------------------------------------------------------------------------------------------------