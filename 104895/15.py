'''Введём выражение M & K, обозначающее поразрядную конъюнкцию M и K
 (логическое «И» между соответствующими битами двоичной записи).
  Определите наименьшее натуральное число A, такое что выражение
(X & 13 = 0) → ((X & 40 ≠ 0) → (X & A ≠ 0))

тождественно истинно (то есть принимает значение 1 при любом натуральном значении переменной X)?'''

def f (m,k):
	k = bin(k)
	m = bin(m)
	k = k[2::]
	m = m[2::]
	if len(m)>len(k):
		k = '0'*(len(m)-len(k))+k
	else:
		m = '0'*(len(k)-len(m))+m
	l = ''
	for i in range (len(m)):
		p = int (k[i])
		f = int (m[i])
		l = str(f*p)+l
	if int(l)==0:
		return True
	else:
		return False

for a in range (1000):
	d = 0
	for x in range (1000):
		if (f(x,13)<=(not(f(x,40))<=f(x,a)))==0:
			d=1
			break
	if d==0:
		print (a)
		break