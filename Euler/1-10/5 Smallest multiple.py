def gcm(a, b):
    while a != 0 and b != 0:
        if a > b: a %= b
        else: b %= a
    return max(a,b)

def lcm(a, b):
    return a*b // gcm(a, b)

def reduce(func, n):
    x = 1
    for i in range(2, n):
        x = func(x, i)
        print(x)
    return x

print(reduce(lcm, 20))