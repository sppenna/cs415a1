

def consecutiveIntegerGCD(m, n):
    if m == 0:
        print("invalid input")
        return
    elif (n == 0):
        print("invalid input")
        return
    if m < n:
        t = m
    else:
        t = n
    if m % t == 0 and n % t == 0:
        return t

    while (m % t != 0 and n % t != 0):
        if m % t == 0:
            return t
            if n % t == 0:
                return t
        t = t - 1
