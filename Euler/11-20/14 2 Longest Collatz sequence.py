import operator
ll = list()
def collatz(len, num):
    if num >= 10**6:
        ll.append((num, len))
        print(num, len)
        return 0
    collatz(len+1, num*2)
    if (num - 1)%3 == 0:
        collatz(len+1,int((num - 1)/3))
collatz(1,1)
sorted = sorted(ll, key=operator.itemgetter(1))
print(sorted)