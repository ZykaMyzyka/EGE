with open('24-s1.txt','r') as f:
	a = f.read().splitlines()
n = 0
for i in range (len(a)):
	for j in range (len(a[i])-2):
		if a[i][j]=='A' and a[i][j+2]=='R':
			n+=1
			break 
print (n)