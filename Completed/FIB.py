#find total number of rabbit pairs after n months with k new pairs per generation
#The population begins in the first month with a pair of newborn rabbits.
#Rabbits reach reproductive age after one month.
#In any given month, every rabbit of reproductive age mates with another rabbit of reproductive age.
#Exactly one month after two rabbits mate, they produce one male and one female rabbit.
#Rabbits never die or stop reproducing.

n = 28
k = 3
#recursive fibonnaci def 

#list of adult rabbit pairs
adult = 0
#maturing
maturing = 0
#list of young rabbit pairs
young = 1
i = 1
while i <= n:
    #maturing become adults
    adult += maturing
    maturing = 0
    #young become maturing
    maturing += young
    young = 0
    #adults mate 3x new young
    young = adult * k
    print("generation", i)
    print("adult " , adult)
    print("maturning" , maturing)
    print("young " ,young)
    i+=1
print(adult+maturing)


