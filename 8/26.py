k=30
m=10
a=[]
b=[]
with open('26-k5.txt','r') as f:
    s=f.read().splitlines()
for i in range(len(s)):
    s[i]=int(s[i])
s.sort()
for i in range(0,k):
    a.append(s[i])

s.reverse()
for i in range(0,m):
    b.append(s[i])
print(min(b))
n=0
for i in range(len(a)):
    n=n+a[i]
print(n/30)
