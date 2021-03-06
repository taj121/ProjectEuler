# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143 ?

import numpy as np

LIMIT = 600851475143

def createArray(limit):
    return np.full((1,LIMIT), True, dtype=bool)

def sieve(p,allNums):
    newP = p
    for x in allNums:
        if x != p and x % p == 0:
            allNums[x] = False
    for x in allNums:
        if x > p and allNums[x]:
            newP = x
    if newP == p:
        return p
    else:
        return sieve(newP, allNums)

print sieve(2, createArray(LIMIT))
