max = [0,0]
for i in range(1,10**6+1):
    x = i
    ll = list()
    ll.append(x)
    while x!=1:
        if x%2 == 0:
            x//=2
        else:
            x*=3
            x+=1
        ll.append(x)
    if ll.__len__() > max[1]:
        max = [i, ll.__len__()]
    #print(ll)
print(max)