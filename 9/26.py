with open('26-k5.txt','r') as f:
    s=f.read().splitlines()
for i in range(len(s)):
    s[i]=int(s[i])
s.sort()
s.reverse()
c=0
b=0
for i in range(0,70):
    c=c+s[i]
for i in range(70,141):
    b=b+s[i]
c=c/70
b=b/70
print(c,b)

