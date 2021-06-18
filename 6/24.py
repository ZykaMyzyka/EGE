m=0
with open('24-s1.txt','r') as f:
    s=f.read().splitlines()
    
for i in range(len(s)):
    e=0
    j=0
    for k in range(len(s[i])):
        if s[i][k]=='J':
            j+=1
        if s[i][k]=='E':
            e+=1
    if j>e:
        m+=1
print(m)
