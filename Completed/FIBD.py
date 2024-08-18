#given n < 100 and m < 20
#how many rabits are there after n months if all live for m months
#start with 1 pair of  rabbits
#need 1 month to reach maturity
#---------------------------------------------------------------------------------------------------
n = 98
m = 18


i = 1
#adult = 0
adult = []
maturing = 0
young = 1
while i <= n:
    #rabbits make new young
    alive = 0
    for a in adult:
        alive+=a
    young += alive

    #rabbits grow up
    adult = [maturing] + adult
    maturing = 0

    #young become maturing
    maturing += young
    young = 0

    #need to keep track of how many are in different age buckets
    #move numbers along in an array
    #if entry in array reaches m -> dead
    #adults die at m months
    if len(adult) >= m:
        adult = adult[:-1]

    print("generation", i)
    print("adult " , adult)
    print("maturing " , maturing)
    print("young " ,young)
    print()
    i+=1
alive = 0
for a in adult:
    alive+=a
print(alive+maturing+young)
#---------------------------------------------------------------------------------------------------
