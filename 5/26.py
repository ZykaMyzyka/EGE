k=1000000
with open('26-j3.txt','r') as f:
    s=f.read().splitlines()
for i in range(len(s)):
    s[i]=int(s[i])
s.sort()
s.reverse()
o=0
n=0
l=0
x1=0
for i in range(len(s)):
    if (n+s[0])<k:
        n=n+s[0]
        l+=1
        x1=s[0]
        del s[0]
m=k-n
for i in range(len(s)):
    if s[i]<=m:
        l+=1
        x1=s[i]
        break
print(l)
print(x1)
print(s)
                
        
        
