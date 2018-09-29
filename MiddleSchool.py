'''
This function takes an input int n that creates a list of all its prime factors

'''
import Sieve





def primeFactor(n: int):
    factorList = []
    primeIndex = 0
    listOfAllPrimes = Sieve.sievePrimes(n)
    p = listOfAllPrimes[primeIndex]
    while p <= n:
        while n % p == 0:
            factorList.append(p[primeIndex])
            n //= p
        primeIndex += 1
        p = listOfAllPrimes[primeIndex]

    return factorList


def main():
    n = 234
    m = 234
    print (Sieve.sievePrimes(m))
    # mPrime = primeFactor(m)
    # print(mPrime)
    # nPrime = primeFactor(n)
    # print(nPrime)


main
