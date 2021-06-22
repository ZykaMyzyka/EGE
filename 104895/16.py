def F( n ):
  if n<=1:
  	return n+1
  elif n > 1:
    d=2*n+n+1
    return d+F(n-1)+F(n-3)

for i in range (10000):
	if F(i)>1000000:
		print (i,F(i))
		break
