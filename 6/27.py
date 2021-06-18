a=[]
b=[]
with open('27-28b.txt','r') as f:
    s=f.read().splitlines()
for i in range(len(s)):
    b=s[i].split()
    for j in range(len(b)):
        b[j]=int(b[j])
    b.sort()
    a.append(b)
n=0
for i in range(len(a)):
    n=n+a[i][0]
aa=[]
if n%8==2:
    for i in range(len(a)):
        k=n-a[i][0]+a[i][1]
        if k%8!=2:
            aa.append(k)

    print(min(aa))
    
if n%8!=2:
    print(n)
    
