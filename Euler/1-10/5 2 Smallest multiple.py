def isMultiple(x, n):    
    for i in range(1, n):
        if x % i != 0:
            return False
    return True

def factorial(n):
    k = 1
    if n > 1: 
        for i in range(1, n + 1):
            k *= i
        return k

n = 20;

for i in range(n, factorial(n) + 1, n):
    if isMultiple(i, n):
        print(i)