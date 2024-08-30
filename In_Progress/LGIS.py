#given n < 10000 
#given a permuted sequence of length n
#return the increasing and decreasing subsequences
#---------------------------------------------------------------------------------------------------
import math
#---------------------------------------------------------------------------------------------------
file = open('./rosalind_lgis.txt', 'r')
for i, line in enumerate(file):
    if i == 0:
        n = int(line.strip())
    else:
        seq = line.strip().split()
print(n)
print(seq)
print("---")
#---------------------------------------------------------------------------------------------------
def find_spot(result, n):
    left = 0
    right = len(result) - 1

    while left <= right:
        mid = (left + right) // 2
        if result[mid] == n:
            return mid
        elif result[mid] > n:
            right = mid - 1
        else:
            left = mid + 1
    
    return left
#---------------------------------------------------------------------------------------------------
def get_increasing(seq):

    M = []
    P = []
    L = 1
    M[0] = 0

    for i in range(len(seq)):
        left = 0
        right = L

        if (seq[M[right -1]] < seq[i]):
            j = right
        else:
            while(right - left > 1):
                mid = math.floor((right + left) /2):
                if seq[<[mid - 1]] < seq[i]:
                    left = mid
                else:
                    right = mid
        j = left


    result = [seq[0]]
    for n in seq:
        if len(result) == 0 or result[-1] < n:
            result.append(n)
            print("add to end", n)  
        else:
            result[bisect_left(result, n)] = n 

    print(result)
    return result
#---------------------------------------------------------------------------------------------------
for i in get_increasing(seq):
    print(i, end = " ")
print()
#---------------------------------------------------------------------------------------------------