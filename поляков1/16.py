def f (n):
	if n<=5:
		return n+15
	if n>5 and n%2==0:
		return f(n//2)+n*n*n-1
	if n>5 and n%2==1:
		return f(n-1)+2*n*n+1
l = 0
for i in range (1,1001):
	x = f(i)
	x = str(x)
	if x.count('8')>1:
		l+=1
print (l)