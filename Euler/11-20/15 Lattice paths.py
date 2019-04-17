import math


def lpaths(gs):
    return math.factorial(gs * 2) / math.factorial(gs)**2

print(lpaths(20))