a=[]
b=[]
c=[]
m=0
with open('27-31b.txt','r') as f:
    s=f.read().splitlines()
for i in range(len(s)):
    b=s[i].split()
    for j in range(len(b)):
        b[j]=int(b[j])
    b.sort()
    a.append(b)
for i in range(len(a)):
    m=m+a[i][0]+a[i][1]
if m%9==0:
    for i in range(len(a)):
        k=m-a[i][1]+a[i][2]
        if k%9!=0:
            c.append(k)
    print(min(c))
else:
    print(m)
