#find longest common substring

#read input
#---------------------------------------------------------------------------------------------------
import argparse
import os

#cmd line parser
parser = argparse.ArgumentParser(description='Enter Fasta File')
parser.add_argument('-f', type=str)
args = parser.parse_args()

#check if path exists
if os.path.exists(args.f):
    file = open(args.f,'r')
else:
    print("Please enter a valid path")
    exit()

#---------------------------------------------------------------------------------------------------
names = []
dna = []
counter = -1
newseq = False
for line in file:
    if(line[0] == '>'):
        names.append(line.strip()[1::1])
        counter += 1
        newseq = True
    else:
        if newseq:
            dna.append(line.strip())
            newseq = False
        else:
            dna[counter] += line.strip()
#---------------------------------------------------------------------------------------------------
#find shortest pattern
shortestLen = float('inf')
shortestSeq = ""
for seq in dna:
    if len(seq) < shortestLen:
        shortestLen = len(seq)
        shortestSeq = seq
#---------------------------------------------------------------------------------------------------
#build combinded string
combindedString = ""
for count, seq in enumerate(dna):
    combindedString += seq
    combindedString += "$" + str(count)
#print(combindedString)
#---------------------------------------------------------------------------------------------------
#make array of indexes of sentinal values and give them colors
i = 0
lastIndex = -1
colorIndexArray = []
while i < len(combindedString):
    if combindedString[i].isnumeric():
        #continue checking until non numeric or end of string
        lastIndex = i
    else:
        if lastIndex != -1:
            colorIndexArray.append(lastIndex)
        lastIndex = -1
    i += 1
#need to add last index as well
colorIndexArray.append(len(combindedString))
#for entry in colorIndexArray:
    #print(entry)
#---------------------------------------------------------------------------------------------------
#build suffix array
suffixArray = []
for count, letter in enumerate(combindedString):
    #remove all unique seperators from beginning
    if letter.isalpha():
        suffixArray.append(count)
#---------------------------------------------------------------------------------------------------
#quicksort
def partition(arr, low, high):
    i = (low-1)         
    pivot = arr[high]   
    for j in range(low, high):
        #compare both elements
        if combindedString[arr[j]:] < combindedString[pivot:]:
            i = i+1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i+1], arr[high] = arr[high], arr[i+1]
    return (i+1)

def quickSort(arr, low, high):
    if len(arr) == 1:
        return arr
    if low < high:
        pi = partition(arr, low, high)
        quickSort(arr, low, pi-1)
        quickSort(arr, pi+1, high)
#---------------------------------------------------------------------------------------------------
#sort suffix array
quickSort(suffixArray, 0, len(suffixArray)-1)
#for e in suffixArray:
    #print(e)
#---------------------------------------------------------------------------------------------------
#build lcp
lcp = []
letterMatch = 0
for elem in range(1 , len(suffixArray)):
    #compare adjacent strings and see how many commom prefixes they have
    for a,b in zip(combindedString[suffixArray[elem-1]:], combindedString[suffixArray[elem]:]):
        if a == b:
            letterMatch +=1
        else:
            break
    #print(combindedString[suffixArray[elem-1]:], combindedString[suffixArray[elem]:], letterMatch)
    lcp.append(letterMatch)
    letterMatch = 0
#---------------------------------------------------------------------------------------------------
#fill finalArray STEP 1

finalArray = []



#---------------------------------------------------------------------------------------------------
#find lcsm
windowLCP = 0
windowLCS = 0
window_size = 1
LCS = []
LCS_length = 0
#for every entry in lcp and suffix array
#for i in zip(lcp, suffixArray):
    #check if window contains all special values from $0-$(num of inputs)
    #for j in range(0, window_size):
        

    #if yes find min(lcp in the window) ignore the top value on the lcp stack 
    #else expand window down and check again
    
    #record longest found lcs candidate
#continue through the whole array

#TODO add a color to each entry in suffix array 
#add array to keep track of index where sentinal values are DONE
#then give each index its "color" in the form of the number of the sentinal value it has (the one on the end of that word)

#TODO make lists [color, lcp, suffix index]
# STEP 1 [[-1, -1, suffix index]]
# STEP 2 [[-1, -1, suffix index]] sorted
# STEP 3 [[color, -1, suffix index]] *the first colorIndexArray that is larger than the suffix indexs is that indexes color 
#NOTE need to sort the suffix array before making lcp
# STEP 4 [[color, lcp, suffix index]] *rewrite to work with the new list of lists
