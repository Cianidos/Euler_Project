counter,x = 0,1
while True:
    x+=1
    s=0
    for i in range(2,x):
       if x% i == 0 and i!=x and i!=1:
           s+=1
    if s == 0:
        counter+=x
        print("{}# {}".format(counter,x))
    if x>2*10**6:
        print(counter)
        break
