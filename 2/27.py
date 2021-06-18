a=[]
b=[]
c=[]
a1=[]
with open('27.txt','r') as f:
    s=f.read().splitlines()
for i in range(0,len(s)):
    a=s[i].split()
    for j in range(3):
        a[j]=int(a[j])
    a.sort()
    b.append(a)
m=0
for x in range(len(b)):
    m=m+b[x][0]
if m%11!=0:
    for i in range(len(b)):
            c.append(m-b[i][0]+b[i][1])
    for i in range(len(b)):
            c.append(m-b[i][0]+b[i][2])
            
a=[]            
for i in range(len(c)):
    if c[i]%11==0:
        a.append(c[i])
print(min(a))

