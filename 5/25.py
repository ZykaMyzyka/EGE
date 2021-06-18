b=[]
for i in range(251811, 251826):
    a=[]
    for j in range(1,i+1):
        if i%j==0:
            a.append(j)
            if len(a)>4:
                a=[]
                break
    if len(a)==4:
        b.append(a)
for i in range(len(b)):
    print(b[i][2],b[i][3])
        
            
    
