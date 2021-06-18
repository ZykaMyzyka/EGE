a='ABCD'
b=[]

for x in range(len(a)):
    n=a[x]
    for y in range(len(a)):
        k=n+a[y]
        for z in range(len(a)):
            l=k+a[z]
            b.append(l)
            
m=0
for i in range(len(b)):
    if (('BC' in b[i]) or ('CB' in b[i]))==False:
        if 'A' in b[i]:
            if (('AD' in b[i]) or ('DA' in b[i])) and not(('AAD' in b[i]) or ('DAA' in b[i]))==True:
                m+=1

        else:
            m+=1
        
        
print(m)
    
