from CommonElements import *
from ConsecutiveInt import *
from Euclid import *
#middle school and Sievenot working
#from MiddleSchool import *
#from Sieve import *
from fibonacci import *
import matplotlib.pyplot as plt
import random as rand

#Testing Average case for Euclid's algorithm size 5
n, x = 5, 1
euclidAvg = []
xaxis = []
while n < 100:
    xaxis.append(n)
    i = 1
    count = 0
    tmp = []
    while i < n+1:
        tmp.append(euclidGCD(n, i, count))
        i+=1
        count = 0
    euclidAvg.append(float(sum(tmp))/float(len(tmp)))
    n+=1
#This is the average number of % for Euclids

#consecutive integer

n, x = 5, 1
consAvg = []
xaxis = []
while n < 100:
    xaxis.append(n)
    i = 1
    count = 0
    tmp = []
    while i < n+1:
        tmp.append(consecutiveIntegerGCD(n, i, count))
        count = 0
        i+=1
    consAvg.append(float(sum(tmp))/float(len(tmp)))
    n+=1
#This is the average number of % for Euclids
#print("euclidGCD:", euclidAvg)
#print("ConsecutiveIntegerGCD:", consAvg)
plt.title("GCD (Euclid vs Consecutive Integer)")
plt.scatter(xaxis, euclidAvg, label="Euclid's")
plt.scatter(xaxis, consAvg, label="Consecutive Int")
plt.legend()
plt.show()

#generate fibonacci sequence of size 20
i = 100
fibList = fib(i)
#print(fibList)
fibEuclid = []
xaxis = []
n = 1
#test worst case Euclids algorithm on each consecutive Fibonacci sequence
while n < i-1:
    xaxis.append(n)
    count = 0
    fibEuclid.append(euclidGCD(fibList[n+1], fibList[n], count))
    n+=1

print("Worst Case Euclid's Algorithm:", fibEuclid)
plt.scatter(xaxis, fibEuclid)
plt.title("Euclid's Worst Case")
plt.show()

#demonstrate complexity of finding common elements
i = 0
list1, list2, output, numIters, xaxisGamma, xaxisBigO = [], [], [], [], [], []

while i < 100:
    n = rand.randint(1, 10)
    m = rand.randint(1, 10)
    j, y, count = 0, 0, 0
    #generate 2 lists of n size full of random numbers
    while j < n:
        list1.append(rand.randint(1,100))
        j+=1
    while y < m:
        list2.append(rand.randint(1,100))
        y+=1
    #sort both lists in ascending order
    list1.sort()
    list2.sort()
    #add the max of list1 and list2 to xaxis
    xaxisGamma.append(max(len(list1), len(list2)))
    xaxisBigO.append(len(list1)+len(list2))
    numIters.append(comElems(list1, list2, output, count))
    i+=1
xaxisBigO.sort()
xaxisGamma.sort()
line_mid = plt.scatter(xaxisBigO, numIters, label="Theta")
line_up = plt.plot(xaxisBigO, xaxisBigO, label="Big O")
line_down = plt.plot(xaxisBigO, xaxisGamma, label="Gamma")
plt.legend()
plt.title("Common Element Finder")
plt.show()
