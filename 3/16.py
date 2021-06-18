i=0
a=[]
for n in range(1,1001):
    if n<=13:
        i=n*n*n + n*n + 1
        a.append(i)
    if n>13 and n%3==0:
        i=a[n-2] + 2*n*n - 3
        a.append(i)
    if n>13 and n%3!=0:
        i=a[n-3]+3*n + 6
        a.append(i)
n=0
j=0
for i in range(len(a)):
    a[i]=str(a[i])
    if ('0' in a[i]) or ('2' in a[i]) or ('4' in a[i]) or ('6' in a[i]) or ('8' in a[i]):
        j=0
    else:
        n+=1
print(n)
