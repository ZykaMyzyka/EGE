def f(n):
    if n>25:
        return n*n+2*n+1
    if n<=25 and n%2==0:
        return 2*f(n+1)+f(n+3)
    if n<=25 and n%2!=0:
        return f(n+2)+3*f(n+5)
m=0
k=0
for n in range(1,1001):
    x=str(f(n))
    if '0' in x:
        m=0
    else:
        k+=1
print(k)
