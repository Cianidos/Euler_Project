from itertools import combinations, combinations_with_replacement,permutations
import numpy as np


def primes_gen(n):
    if n < 2:
        return 0
    if n == 2:
        return 2
    if n % 2 == 0:
        n += 1
    primes = [True] * n
    primes[0], primes[1] = [None] * 2
    sum = 0
    for ind, val in enumerate(primes):
        if val is True and ind > n ** 0.5 + 1:
            if ind>1000 and not "0" in str(ind):
                yield (ind)
        elif val is True:
            primes[ind * 2::ind] = [False] * (((n - 1) // ind) - 1)
            if ind > 1000 and not "0" in str(ind):
                yield (ind)


primes = set(primes_gen(10000))
intersepts = set()
for i in primes:
    a = frozenset(sorted(int(i[0]+i[1]+i[2]+i[3]) for i in permutations(str(i),4)))
    intersepts.add(frozenset(sorted(a.intersection(primes))))
    print(a.intersection(primes))
    #print("{}  {}".format(i,a))
print()