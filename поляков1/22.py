for i in range (101,1000):
	x = i
	l = x
	m = 65
	if l%2==0:
		m = 52
	while l!=m:
		if l>m:
			l = l-m
		else:
			m = m-l
	if m ==26:
		print (i)
		break
