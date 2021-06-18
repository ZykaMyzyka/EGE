for A in range(1,1200):
    n=0
    for x in range(1,1200):
        if ((x%19!=0 or x%15!=0) <= (x%A!=0))==True:
            n+=1
    if n==1199:
        print(A)
        break
