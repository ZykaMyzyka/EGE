for A in range(1,1200):
    n=0
    for x in  range(1,1200):
        if ((x%A==0 and x%16==0) <= (x%16!=0 or x%24==0))==True:
            n+=1
    if n==1199:
        print(A)
        break
