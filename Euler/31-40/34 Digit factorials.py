import math
res = 0
for j in range(3,10000000):

    sum = 0
    for i in str(j):
        sum+=math.factorial(int(i))
    if sum == j: res+=j
    print("{}    {}".format(j,sum))
print(res)