fibList = [0, 1]
size = 10
for i in range(2,size):
    fibList.append(fibList[i-1]+fibList[i-2])
print(fibList)
