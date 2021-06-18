b=[]
for i in range(135743,135790):
    a=[]
    for j in range(1,i+1):
        if i%j==0:
            a.append(j)
            if len(a)>6:
                a=[]
                break
    if len(a)==6:
        b.append(a)
for i in range(len(b)):
    print(b[i][4],b[i][5])

        
