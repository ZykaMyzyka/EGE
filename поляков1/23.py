a = [0]*375
a[2]=1
for i in range (3,375):
	a[i]=a[i-1]
	if i-3>1:
		a[i]+=a[i-3]
	if i**0.5%1==0 and i**0.5>=2:
		a[i]+=a[int(i**0.5)]
print (a)