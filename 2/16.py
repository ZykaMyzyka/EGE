a=[]
i=0
for n in range(1,801):
    if n<=18:
        i=n+3
        a.append(i)
    if n>18 and n%3==0:
        i=(n//3)*a[(n-1)//3]+n-12
        a.append(i)
    if n>18 and n%3!=0:
        i=a[n-2]+n*n+5
        a.append(i)
n=0
for j in range(len(a)):
    a[j]=str(a[j])
    if ('1' in a[j]) or ('3' in a[j]) or ('5' in a[j]) or ('7' in a[j]) or ('9' in a[j]):
        n=n
    else:
        n+=1
print(n)       
