for a in range (1,1001):
	d = 0
	for x in range (1,1001):
		if (((x%a==0) and (x%24==0) and (x%16!=0))<=(x%a!=0))==False:
			d+=1
			break
	if d ==0:
		print (a)
		break
