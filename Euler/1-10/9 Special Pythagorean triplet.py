for a in range(1000):
    for b in range(a,1000):
        for c in range(b,1000):
            if a**2 + b**2 == c**2 and a+b+c==1000:
                print("{} {} {}".format(a,b,c))
                print(a*b*c)
