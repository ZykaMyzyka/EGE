n = 1000
a = []
for i in range (1000):
	k = float(input())
	a.append(k)
p =-1000000000
k = 0
for i in range (1,1000):
	if (abs(a[i]-a[i-1]))>20:
		k +=a[i]
	elif (abs(a[i]-a[i-1]))<20:
		if p<k:
			p=k
		k = 0
print (p)