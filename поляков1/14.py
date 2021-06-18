s = 9**7+3**8-5
n0=0
n1=0
n2=0
while s>0:
	if s%3==0:
		n0+=1
	elif s%3==1:
		n1+=1
	elif s%3==2:
		n2+=1
	s = s//3
print (n0,n1,n2)