ddd ={}
k = 10000
for x in range(k+1):
    ll = [1]
    for j in range(2, round(x ** 0.5) + 1):
        if x // j <= j:
            break
        if x % j == 0:
            ll.append(j)
            ll.append(x // j)
    print("{} {}".format(x, ll))
    ddd.update({x:sum(ll)})
sum = 0
for i in range(k+1):
    if i == ddd.get(ddd.get(i)) and i!=ddd.get(i):
        print("{} {}".format(i,ddd.get(i)))
        sum+=i
print(ddd)
print(sum)
