#given k m n. homozygous dominant, heterozygous, homozygous recessive
#probability that 2 random organisms produce offspring with a dominant allele 
k = 20
m = 17
n = 20
su = k + m + n

#probability of 2 dominant
pdomdom = k/su * ((k-1)/(su-1))
#probability of dominant + hetero
pdomhet = k/su * (m/(su-1))
#probability of hetero + dominant
phetdom = m/su * (k/(su-1))
#probability of dominant + recessive
pdomrec = k/su * (n/(su-1))
#probability of recessive + dominant
precdom = n/su * (k/(su-1))
#probability of 2 hetero
phethet = m/su * ((m-1)/(su-1))
#probability of hetero + recessive
phetrec = m/su * (n/(su-1))
#probability of recessive + hetero
prechet = n/su * (m/(su-1))

total = pdomdom + pdomhet + phetdom + pdomrec + precdom + (phethet*.75) + (phetrec*.5) + (prechet*.5)
print(total)



