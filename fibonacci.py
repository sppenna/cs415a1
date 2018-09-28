def fib(n):
    fibList = [0, 1]
    for i in range(2,n):
        fibList.append(fibList[i-1]+fibList[i-2])
    return fibList