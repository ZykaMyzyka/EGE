a=[]
b=[]
with open('27-26a.txt','r') as f:
    s=f.read().splitlines()
for i in range(len(s)):
    x=s[i].split()
    for j in range(len(x)):
        x[j]=int(x[j])
    x.sort()
    a.append(x)
n=0
for i in range(len(a)):
    n=n+a[i][0]
if n%16==15:
    print(n)
if n%16!=15:
    for i in range(len(a)):
        j=n-a[i][0]+a[i][1]
        if j%16==15:
            b.append(j)
print(min(b))

