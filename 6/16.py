op=0
a=[]
def f(n):
    if n>25:
        return n*n+4*n+3
    if n<=25 and n%3==0:
        return f(n+1) + 2*f(n+4)
    if n<=25 and n%3!=0:
        return f(n+2) +3*f(n+5)

for n in range(1,1001):
    x=str(f(n))
    a.append(x)
for i in range(len(a)):
    c=0
    for j in range(len(a[i])):
        m=int(a[i][j])
        c=c+m
    if c==24:
        op+=1
        
print(op)
