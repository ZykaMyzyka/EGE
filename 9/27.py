a=[]
b=[]
with open('27-25b.txt','r') as f:
    s=f.read().splitlines()
for i in range(len(s)):
    x=s[i].split()
    for j in range(len(x)):
        x[j]=int(x[j])
    x.sort()
    a.append(x)
n=0
for i in range(len(a)):
    n=n+a[i][1]
if n%8==3:
    print(n)
if n%8!=3:
    for i in range(len(a)):
        j=n-a[i][1]+a[i][0]
        if j%8==3:
            b.append(j)
print(max(b))

