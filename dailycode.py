## PRINTS 1 - 100
## multiples of 3 print fizz
##multiples of 5 print Buzz
## Both 3 and 5  FizzBuzz
"""
## Michael Zhang and Sean Osier

for i in range(1,100):
    bythree = i%3
    byfive = i%5
    if (bythree == 0) and (byfive == 0):
        print "FizzBuzz"
    elif bythree == 0:
        print "Fizz"
    elif byfive == 0:
        print "Buzz"
    else:
        print i


##Michael and David

def reverser(s):
    print  s[::-1]

reverser("first\nsecond")

import sys

for line in sys.stdin:
    print line[::-1].replace('\n','') + '\n'

##Michael Zhang And John Keating

#Objective: Maximize sum of 13 adjacent digits in 1000 digit number

s = "7316717653133062491922511967442657474235534919493496983520312774506326239578318016984801869478851843858615607891129494954595017379583319528532088055111254069874715852386305071569329096329522744304355766896648950445244523161731856403098711121722383113622298934233803081353362766142828064444866452387493035890729629049156044077239071381051585930796086670172427121883998797908792274921901699720888093776657273330010533678812202354218097512545405947522435258490771167055601360483958644670632441572215539753697817977846174064955149290862569321978468622482839722413756570560574902614079729686524145351004748216637048440319989000889524345065854122758866688116427171479924442928230863465674813919123162824586178664583591245665294765456828489128831426076900422421902267105562632111110937054421750694165896040807198403850962455444362981230987879927244284909188845801561660979191338754992005240636899125607176060588611646710940507754100225698315520005593572972571636269561882670428252483600823257530420752963450"




t = [int(i) for i in s ]

count1 = 0
count2 = 13
#for i in t:

biggest = 0

while count2 <= 1000:
    numslice = t[count1:count2]
    
    mult = reduce(lambda x,y: x*y, numslice, 1)   # REDUCE PROCESSING METHOD: takes 2 variables x, y. creates 1 variable x*y, from a list
                                                  # reduce goes through list in pairs. first pair multiply. takes answer then multiplies by next item. "peels" items off list.
    count1 += 1
    count2 += 1


    if mult > biggest:
        biggest = mult 

print biggest

"""

import numpy as np
#import matplotlib.pyplot as plt


data = [2, 7 , 1 , 5,  10]

candidate = float(0.0)
start = float('inf')

xarray = []
yarray = []

while candidate <= 9.9:
    num = [(i-candidate)**2 for i in data]
    total = sum(num)
    total 
    if total <= start:
        start = total

    xarray.append(candidate)
    yarray.append(total)
    candidate += float(0.1)

    #print num
    

    #print total
    #print start

print len(xarray)