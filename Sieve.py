'''
Finds Prime Numbers 2 - n and stores them in a list

'''


def sievePimes(n: int) -> list:
    primeList = []
    for h in range(2, n):
        primeList.append(h)
    for i in range(2, n):
        for j in range(i, n):
            k = i * j
            if k in primeList:
                primeList.remove(k)
    print(primeList)
    return primeList

