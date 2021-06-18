for i in range(3532000,3532160):
    n=0
    for j in range(2,6000):
        if i%j==0:
            n+=1
    if n==0:
        print(i-3531999, i)
