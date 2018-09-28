

def consecutiveIntegerGCD(m, n, count):
    if m == 0:
        print("invalid input")
        return count
    elif (n == 0):
        print("invalid input")
        return count
    if m < n:
        t = m
    else:
        t = n

    while (t > 0):
        count+=1
        if m % t == 0:
            if n % t == 0:
                count+=1
                return count
        t-=1
