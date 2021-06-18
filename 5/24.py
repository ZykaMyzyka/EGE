A=0
with open('24-s1.txt','r') as f:
    s=f.read().splitlines()
for i in range(len(s)):
    k=0
    u=0
    for j in range(len(s[i])):
        if s[i][j]=='K':
            k+=1

        if s[i][j]=='U':
            u+=1
    if k>u:
        A+=1
print(A)
