with open('26-j1.txt','r') as f:
    s=f.read().splitlines()
for i in range(len(s)):
    s[i]=int(s[i])
m=0
for j in range(120):
    for i in range(0,100):
        if (i in s) and (100-i in s):
            s.remove(i)
            s.remove(100-i)
            m+=1
print(m)

    
