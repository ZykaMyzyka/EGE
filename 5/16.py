i=0
a=[]
b=[]
for n in range(1,1001):
    if n<=15:
        i=n*n+3*n+9
        a.append(i)
    if n>15 and n%3==0:
        i=a[n-2]+n-2
        a.append(i)
    if n>15 and n%3!=0:
        i=a[n-3]+n+2
        a.append(i)
for i in range(len(a)):
    a[i]=str(a[i])
j=0
m=0
for i in range(len(a)):
    if ('1' in a[i]) or ('3' in a[i]) or ('5' in a[i]) or ('7' in a[i]) or  ('9' in a[i]):
        j=0
    else:
        m+=1
print(m)
