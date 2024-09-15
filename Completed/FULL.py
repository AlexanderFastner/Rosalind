#given a list of numbers (2n + 3), the first being the parent mass
#return the center of the peptide of length n
#---------------------------------------------------------------------------------------------------
#sort list
#difference between weight is the AA
#match rigth left sring for top bottom of list
#answer
#---------------------------------------------------------------------------------------------------
monoisotopic={
"A":71.03711,
"C":103.00919,
"D":115.02694,
"E":129.04259,
"F":147.06841,
"G":57.02146,
"H":137.05891,
"I":113.08406,
"K":128.09496,
"M":131.04049,
"N":114.04293,
"P":97.05276,
"Q":128.05858,
"R":156.10111,
"S":87.03203,
"T":101.04768,
"V":99.06841,
"W":186.07931,
"Y":163.06333,
}
#---------------------------------------------------------------------------------------------------
with open ("./rosalind_full.txt", 'r') as inputs:
    IN= inputs.read().split()
    L= [round(float(i), 7) for i in IN]
tot = L[0]
L = L[1:]
print("tot", tot)
print("L", L)
L.sort()
print("L sort", L)
print()
#---------------------------------------------------------------------------------------------------
def find_closest_value(dictionary, target):
    closest_key = min(dictionary, key=lambda k: abs(dictionary[k] - target))
    return closest_key

def find_closest_value_distance(dictionary, target):
    closest_key = min(dictionary, key=lambda k: abs(dictionary[k] - target))
    return abs(dictionary.get(closest_key) - target)

#build pairs with total length
def find_pairs(L):
    pairs = []
    array = L
    #print(array)
    while len(array) > 0:
        c = array[0]
        i = array[-1]
        pairs.append([c, i])
        # print(c, " ", i)
        array.remove(c)
        array.remove(i)
        #remove both from array
    return pairs

def find_largest_within_limit(arr, limit):
    result = float('-inf')
    for num in arr:
        if num <= limit and num > result:
            result = num
    return result if result != float('-inf') else None

def side_sort(p):
    left = [p[0][0]]
    right = [p[0][1]]
    p = p[1:]
    for i in p:
        print()
        print("left", left)
        print("right", right)
        print()
        print(i[0])
        next = find_largest_within_limit(left, i[0])

        diff = i[0] - next
        print("diff: ", diff)
        dist = find_closest_value_distance(monoisotopic, diff)
        print("dist", dist)

        if diff > 57 and diff < 187 and dist < 0.00001:
            #possible 
            left.append(i[0])
            right.append(i[1])
        else:
            left.append(i[1])
            right.append(i[0])
    left.sort()
    right.sort()
    print(left)
    print(right)
    return left, right

def get_aa(left, right):
    i = 1
    ansl = []
    ansr = []
    while i < len(l):
        prevl = l[i-1]
        prevr = r[i-1]
        print(l[i] - prevl)
        ansl.append(find_closest_value(monoisotopic, l[i] - prevl))
        ansr.append(find_closest_value(monoisotopic, r[i] - prevr))
        i+=1
    ansr.reverse()
    ansl = ''.join(ansl)
    ansr = ''.join(ansr)
    if ansl == ansr:
        print("matching")
    return ansl
#---------------------------------------------------------------------------------------------------
p = find_pairs(L)
#print("p", p)
#check which side the length might belong too
l, r = side_sort(p)
print(get_aa(l,r))

#---------------------------------------------------------------------------------------------------