with open('24-s1.txt','r') as f:
    s=f.read().splitlines()
m=0
for i in range(len(s)):
    if 'YZ' in s[i]:
        s[i]=s[i].replace('YZ','00',1)
    if 'YZ' in s[i]:
        m+=1
print(m)
    
