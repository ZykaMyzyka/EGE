for A in range(1,1200):
    n=0
    for x in range(1,1200):
        if ((x%A==0) <= (x%28!=0 or x%42==0))==True:
            n+=1
    if n==1199:
        print(A)
        break
