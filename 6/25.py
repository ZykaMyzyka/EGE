a=[]
for i in range( 338472,338495):
    for j in range(1,i+1):
        if i%j==0:
            a.append(j)
            if len(a)>4:
                a=[]
                break
    if len(a)==4:
        print(a[3],a[2])
        a=[]
    else:
        a=[]
    
    
