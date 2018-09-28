'''
To print this function use print(EuclidGCD(m,n))
'''
#import sys
#import setuptools


def euclidGCD(m, n, count):
    while(n):
        m, n = n, m % n
        count+=1
    return count
'''
    if n > n:
        if n % m == 0:
            return m
        else:
            return euclidGCD(n % m, m, count)
    else:
        count+=1
        if m % n == 0:
            return n
        else:
            return euclidGCD(n, m % n, count)
'''

