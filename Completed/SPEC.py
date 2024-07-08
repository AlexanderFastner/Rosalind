#---------------------------------------------------------------------------------------------------
#calculate the proable protein from mass spec weights
#---------------------------------------------------------------------------------------------------
#given a list L of weights
#return the likley Protein sequence
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
#add exception for I/L
#just remove L and always choose I
#"L":113.08406,
#---------------------------------------------------------------------------------------------------

with open ("./rosalind_spec.txt", 'r') as inputs:
    IN= inputs.read().split()
    L= [float(i) for i in IN]
print("L", L)

def find_closest_value(dictionary, target):
    closest_key = min(dictionary, key=lambda k: abs(dictionary[k] - target))
    return closest_key

i=1
predicted_protein=[]
while i < len(L):
    print(L[i])
    residue_weight=L[i]-L[i-1]
    predicted_protein.append(find_closest_value(monoisotopic, residue_weight))
    i+=1

for res in predicted_protein:   
    print(res, end='')
print()
#---------------------------------------------------------------------------------------------------