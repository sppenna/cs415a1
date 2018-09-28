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
while n < 51:
    xaxis.append(n)
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
plt.scatter(xaxis, euclidAvg)
plt.title("Euclid's Algorithm Average")
plt.show()

#consecutive integer

n, x = 5, 1
consAvg = []
xaxis = []
while n < 51:
    xaxis.append(n)
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

#generate fibonacci sequence of size 20
i = 20
fibList = fib(i)
#print(fibList)
fibEuclid = []
xaxis = []
n = 5
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
list1, list2, output, numIters, xaxis = [], [], [], [], []

while i < 5:
    n = rand.randint(1, 20)
    j, count = 0, 0
    #generate 2 lists of n size full of random numbers
    while j < n:
        list1.append(rand.randint(1,100))
        list2.append(rand.randint(1,100))
        j+=1
    #sort both lists in ascending order
    list1, list2 = (list(x) for x in zip(*sorted(zip(list1, list2), key=lambda pair: pair[0])))
    #add the size of the two lists to the xaxis
    xaxis.append(len(list1) + len(list2))
    numIters.append(comElems(list1, list2, output, count))
    i+=1
xaxis.sort()
print("sizes of list1+list2", xaxis)
print("number of increments", numIters)
plt.scatter(xaxis, numIters)
plt.title("Common Element Finder")
plt.show()
