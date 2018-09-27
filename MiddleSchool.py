'''
This function takes an input int n that creates a list of all its prime factors

'''
import Sieve

def primeFactor(n: int):
    factorList = []
    primeList = Sieve.sievePrimes(n)
    k = n
    for i in range(len(primeList)):
        while k % primeList[i] == 0:
            factorList.append(primeList[i])
            k = k // primeList[i]

    print(factorList)

