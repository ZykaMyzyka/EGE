with open('24-j5.txt','r') as f:
    s=f.read().splitlines()
m=0
while 'SOCKS' in s[0]:
    s[0]=s[0].replace('SOCKS','',1)
    m+=1
print(m)
