n = int (input())
m = 0
a = []
for i in range (n):
	k = int (input())
	if k<151:
		m+=k
	else:
		a.append (k)
a.sort()
h = len(a)//2
l = 0
for i in range (len(a)):
	if i<h:
		m+=a[i]*.8
		if l<a[i]:
			l = a[i]
	else:
		m+=a[i]
print (m,l)


