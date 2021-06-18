import statistics
with open('26-j2.txt','r') as f:
    s=f.read().splitlines()
for i in range(len(s)):
    s[i]=int(s[i])
n=statistics.mean(s)
k=statistics.median(s)
n=int(n)
k=int(k)
print(k)
print(n)
m=0
for i in range(n,k+1):
    for j in range(len(s)):
        if s[j]==i:
            m+=1
print(m)
