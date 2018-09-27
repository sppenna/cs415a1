'''
To print this function use print(EuclidGCD(m,n))
'''
import sys
import setuptools



def euclidGCD(m, n):
    if n > n:
        if n % m == 0:
            return m
        else:
            return euclidGCD(n % m, m)
    else:
        if m % n == 0:
            return n
        else:
            return euclidGCD(n, m % n)


