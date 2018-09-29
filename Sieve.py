'''
Finds Prime Numbers 2 - n and stores them in a list

'''


def sievePrimes(n, count):
    """

    """
    count = 0
    primeList = []
    for h in range(1, n):
        primeList.append(h)
    for i in range(2, n):
        for j in range(i, n):
            count+=1
            k = i * j
            if k in primeList:
                primeList.remove(k)
    return count
