for x in range (2):
	for y in range (2):
		for z in range (2):
			for w in range (2):
				if (((y<=x) or (not(z) and w))==(w==x))==True:
					print ('|',x,'|',w,'|',y,'|',z,'|')