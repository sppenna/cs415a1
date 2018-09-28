from CommonElements import *
from ConsecutiveInt import *
from Euclid import *
#middle school and Sievenot working
#from MiddleSchool import *
#from Sieve import *
#from Fibonacci import *
import matplotlib.pyplot as plt

#Testing Average case for Euclid's algorithm size 5
n = 5
euclidAvg = []

i = 1
count = 0
while i < n+1:
    euclidAvg.append(euclidGCD(n, i, count))
    i+=1
    count = 0 
    
#This is the average number of % for Euclids
print(euclidAvg)
xaxis = [1, 2, 3, 4, 5]
plt.plot(xaxis, euclidAvg, 'test')
plt.savefig('test.png', dpi=100)
