with open('24-j5.txt','r') as f:
    s=f.read().splitlines()
m=0
while 'SOCKOS' in s[0]:
    s[0]=s[0].replace('SOCKOS','',1)
    m+=1
print(m)
    
