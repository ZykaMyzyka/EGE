n = 0
l = 0
for i in range (1017,7938,3):
	if i%7!=0 and i%17!=0 and i%19!=0 and i%27!=0:
		n+=1
		if l<i:
			l=i
print (n,l)