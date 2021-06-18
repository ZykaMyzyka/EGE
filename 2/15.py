for A in range(1,1300):
    n=0
    for x in range(1,1200):
        if (not(x%45==0 and x%15!=0) or x%A!=0)==True:
            n+=1
    if n==1199:
        print(A)
        break
        
