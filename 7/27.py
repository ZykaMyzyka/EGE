a=[]
b=[]
k=0
with open('27-27b.txt','r') as f:
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
if n%16==10:
    for i in range(len(a)):
        k=n-a[i][1]+a[i][0]
        if k%16!=10:
            b.append(k)

    print(max(b))
else:
    print(n)
    
