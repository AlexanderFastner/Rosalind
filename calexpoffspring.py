#calculate expected offspring
#given 6 integers correponding to 
#AA-AA  100
#AA-Aa  100
##AA-aa 100
#Aa-Aa 75
#Aa-aa 50
#aa-aa 0
#return expected number of offspring in next generation with the dominant phenotype
#Assuption each couple has 2 offspring
inputset = [18932, 17440, 19225, 17887, 19858, 17633]
output = (inputset[0] * 2) + (inputset[1] * 2) + (inputset[2] * 2) + (inputset[3] * 1.5) + (inputset[4])
print(output)