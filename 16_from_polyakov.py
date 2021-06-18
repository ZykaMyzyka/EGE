#задачи из полякова ссылка: https://kpolyakov.spb.ru/download/ege16.doc

#1
def f(n):
	if n==1:
		return 1
	elif n>1:
		return 2*f(n-1)+n+3
print (f(19))

#2
def z(n):
	if n==1:
		return 3
	else:
		return 2*z(n-1)-n+1
print(z(21))

#11
def g(n):
	if n==1:
		return 1
	elif n>1 and n%2==0:
		return 2*g(n-1)
	elif n>1 and n%2==1:
		return 5*n+g(n-2)
print (g(64))

#56
def r(n):
	if n>20:
		return n*n*n+n
	elif n<=20 and n%2==0:
		return 3*r(n+1)+r(n+3)
	elif n<=20 and n%2!=0:
		return r(n+2)+2*r(n+3)

kolvo=0
for i in range (1,1001):
	k=r(i)
	d = False
	while k>0:
		if k%10==1:
			d = True
		k = k//10
	if d==False:
		kolvo+=1
print (kolvo)

#65
def s(n):
	if n<=5:
		return n+15
	elif n>5 and n%2==0:
		return s(n//2)+n*n*n-1
	elif n>5 and n%2!=0:
		return s(n-1)+2*n*n+1

kolvo = 0
for i in range (1,1001):
	k = s(i)
	d = 0
	while k>0:
		if k%10==8:
			d+=1
		k=k//10
	if d>=2:
		kolvo+=1
print (kolvo)

#73
def q(n):
	if n<50:
		return n
	elif n>49:
		return 2*w(50-n//2)

def w(n):
	if n>40:
		return 10
	elif n<41:
		return 30+q(n+600//n)

print (q(80))

#80(жестко)
# с ответами не сходиться разбираемся
def a(n):
	try:
		if n<=5:
			return n
		elif n>5 and n%3==0:
			return n+a(n/3+2)
		elif n>5 and n%3!=0:
			return n+a(n+3)
	except:
		return False


for i in range (1,1001):
	k=a(i)
	if k!=False:
		if k>1000:
			print (i)
			break

