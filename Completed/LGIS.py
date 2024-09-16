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
int_array = []
for item in seq:
    int_array.append(int(item))
print(int_array)
print("---")
#---------------------------------------------------------------------------------------------------
def get_longest_subsequence(nums, increase=True):
    if not nums:
        return nums

    n = len(nums)
    M = [0] * n  # Indices of potential longest subsequence
    P = [None] * n  # Predecessor array
    L = 0  # Length of the longest subsequence found

    for i in range(n):
        # Binary search
        left, right = 0, L
        while left < right:
            mid = (left + right) // 2
            if (nums[M[mid]] < nums[i]) == increase:
                left = mid + 1
            else:
                right = mid

        # Update predecessor
        if left > 0:
            P[i] = M[left - 1]

        # Update M and L
        M[left] = i
        if left == L:
            L += 1

    # Reconstruct the subsequence
    seq = []
    k = M[L - 1]
    for _ in range(L):
        seq.append(nums[k])
        k = P[k]

    return seq[::-1]
#---------------------------------------------------------------------------------------------------
def join_int_array(arr):
    return " ".join(str(num) for num in arr)
#---------------------------------------------------------------------------------------------------
#longest increasing
print(join_int_array(get_longest_subsequence(int_array)))
print()
print(join_int_array(get_longest_subsequence(int_array, False)))