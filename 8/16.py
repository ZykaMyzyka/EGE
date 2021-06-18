def f(n):
    if n>30:
        return n*n+3*n+5
    if n<=30 and n%2==0:
        return 2*f(n+1)+f(n+4)
    if n<=30 and n%2!=0:
        return f(n+2)+3*f(n+5)
m=0
for n in range(1,1001):
    x=str(f(n))
    k=0
    for i in range(len(x)):
        if x[i]=='0':
            k+=1
            if k>=2:
                m+=1
                break
print(m)
