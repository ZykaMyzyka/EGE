def f(n):
    if n>30:
        return n*n+5*n+4
    if n<=30 and n%2==0:
        return f(n+1) + 3* f(n+4)
    if n<=30 and n%2!=0:
        return 2*f(n+2) + f(n+5)
m=0
for n in range(1,1001):
    x=str(f(n))
    n=0
    for j in range(len(x)):
        n=n+int(x[j])
    if n==27:
        m+=1
print(m)
    
