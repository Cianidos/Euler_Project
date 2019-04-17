from itertools import combinations, combinations_with_replacement,permutations


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
            sum += ind
            yield (ind)
        elif val is True:
            primes[ind * 2::ind] = [False] * (((n - 1) // ind) - 1)
            sum += ind
            yield (ind)



dd = dict()
a = permutations("123456789",4)
a = [int(i[0]+i[1]+i[2]+i[3]) for i in a]
b = list(primes_gen(10000))
a = [i for i in a if i in b and i>999]

for i in a:
    for j in a:
        if i > j and i-j in dd.keys():
            dd[i-j] += [i,j]
        else:
            dd[i-j] = [i,j]

ddd =dict()

for i in sorted(dd.keys()):
    if  i > 0 and len(dd[i]) >2 and i >1000:
        ddd[i] = dd[i]
for i in ddd.keys():
    print("{}   {}".format(i,ddd[i]))

print(a)
