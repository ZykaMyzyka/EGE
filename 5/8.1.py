a='ПРИКАЗ'
b=[]
for q in range(len(a)):
    n=a[q]
    for w in range(len(a)):
        if w!=q:
            m=n+a[w]
        for e in range(len(a)):
            if w!=q and e!=q and e!=w:
                l=m+a[e]
            for r in range(len(a)):
                if w!=q and e!=q and e!=w and r!=w and r!=e and r!=q:
                    k=l+a[r]
                    b.append(k)
m=0
u=0
m=int(m)
for i in range(len(b)):
    m=0
    for j in range(len(b[i])):
        if b[i][j]=='И' or b[i][j]=='A':
            m+=1
    if m==1:
        u+=1
        
            

print(u)
