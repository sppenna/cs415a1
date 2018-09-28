from CommonElements import *
from ConsecutiveInt import *
from Euclid import *
#middle school and Sievenot working
#from MiddleSchool import *
#from Sieve import *
#from Fibonacci import *
import matplotlib.pyplot as plt

#Testing Average case for Euclid's algorithm size 5
n, x = 5, 1
euclidAvg = []
while n < 51:
    i = 1
    count = 0
    tmp = []
    while i < n+1:
        tmp.append(euclidGCD(n, i, count))
        i+=1
        count = 0
    euclidAvg.append(float(sum(tmp))/float(len(tmp)))
    n+=5
#This is the average number of % for Euclids
print("euclidGCD:", euclidAvg)
xaxis = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50]
plt.scatter(xaxis, euclidAvg)
plt.title("Euclid's Algorithm Average")
plt.show()

#consecutive integer

n, x = 5, 1
consAvg = []
while n < 51:
    i = 1
    count = 0
    tmp = []
    while i < n+1:
        tmp.append(consecutiveIntegerGCD(n, i, count))
        count = 0
        i+=1
    consAvg.append(float(sum(tmp))/float(len(tmp)))
    n+=5
#This is the average number of % for Euclids
print("ConsecutiveIntegerGCD:", consAvg)
plt.scatter(xaxis, consAvg)
plt.title("Consecutive Integer Average")
plt.show()
