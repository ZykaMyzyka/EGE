for i in range (174457,174506):
	d = 0
	for j in range (2,int(i**0.5//1)):
		if i%j==0:
			d+=1
			k = j
			l = i//j
		if d>1:
			break
	if d==1:
		print(k,l)