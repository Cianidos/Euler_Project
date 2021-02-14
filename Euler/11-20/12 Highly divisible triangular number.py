x = 1
i = 1
while True:
    ll = []
    i+=1
    x+=i
    for j in range(1, round(x**0.5)+1):
        if x//j <= j:
            break
        if x%j == 0:
            ll.append(j)
            ll.append(x//j)
    print("{} {}".format(x,ll))
    if ll.__len__()>500 :break
print("{} {}".format(x,ll))