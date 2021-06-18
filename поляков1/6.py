for i in range (1000,1,-1):
	s = i
	n = 1
	while s<208:
		s = s+20
		n = n*2
	if n ==256:
		print (i)
		break