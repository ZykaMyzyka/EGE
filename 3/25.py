b=[]
a=[]
for i in range(194455,194501):
    for j in range(1,i+1):
        if i%j==0:
            a.append(j)
        if len(a)>4:
            a=[]
            break
    if len(a)==4:
        b.append(a)
        a=[]
    else:
        a=[]
for i in range(len(b)):
    print(b[i][2],b[i][3])
for i in range(1,194463):
    if 194462%i==0:
        print(i)
        
    
