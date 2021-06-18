import math
a=[]
with open('26-s1 (1).txt', 'r') as f:
    s=f.read().splitlines()
for i in range(0,len(s)):
    a.append(int(s[i]))
a.sort()
n=0
print(a)
for i in range(0,len(a)):
    if a[i]<=100:
        n=n+a[i]
k=0
while k==0:
    if a[0]<=100:
        del a[0]
    else:
        k=1
k=len(a)//2
for i in range(0,k):
    n=n+math.ceil(a[i]*0.9)
for i in range(k,len(a)):
    n=n+a[i]
    

print(a[k-1])
print(n)
