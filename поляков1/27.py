n = int(input())

summ = 0
flag = True
dif = 0
dif1= 0
p = 4	#по условие деление
g = []

for i in range (n):
	a,b,c = map(int, input().split(' '))
	summ+=a+b+c-min(a,b,c)
	k = a+b+c-min(a,b,c)-max(a,b,c)-min(a,b,c)
	g.append (k+k%4/10)
	l = max(a,b,c)-min(a,b,c)
	g.append (l+l%4/10)
g.sort()
g = list(set(g))
print (summ, summ%4)
for i in range (10):
	print(g[i],end = '_')
