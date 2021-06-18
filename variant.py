''' в 25 и 15 ошибка'''



#2
#((x → z) ∧ (z → w)) ∨ (y ≡ (x ∨ z)).
for x in range (2):
	for y in range (2):
		for w in range (2):
			for z in range (2):
				if (((x<=z) and (z<=w)) or (y==(x or z)))==0:
					print (x,y,z,w)
#yzwx

#6
for i in range (1,2000):
	s = i
	n = 0
	while s < s*s:
	  s = s - 1
	  n = n + 3
	if n>2000:
		print (i)
		break

#7
print (72*2*3/4.5)

#8
#Петя составляет шестибуквенные слова перестановкой букв слова АВРОРА. 
#При этом он избегает слов с двумя подряд одинаковыми буквами. Сколько всего различных слов может составить Петя?
from itertools import permutations
a = list(set(list (permutations('АВРОРА', 6))))
n = 0
for i in range (len(a)):
	if a[i][0]==a[i][1] or a[i][2]==a[i][1] or a[i][2]==a[i][3] or a[i][3]==a[i][4] or a[i][4]==a[i][5]:
		pass
	else:
		#print (a[i])
		n+=1
print (n)  

#12
'''НАЧАЛО
  ПОКА нашлось (222)
    заменить (222, 1)
    заменить (111, 2)
  КОНЕЦ ПОКА
КОНЕЦ
Какая строка получится в результате применения приведённой программы к строке вида 1…12…2 (2019 единиц и 2119 двоек)?'''

s = '1'*2019+'2'*2119
while '222' in s:
	s = s.replace('222','1',1)
	s = s.replace('111','2',1)
print (s)

#14
n = 9**9 + 3**21-7
k = 0
while n>0:
	if n%3==0:
		k+=1
	n=n//3
print (k) 


#15
'''Обозначим через ДЕЛ(n, m) утверждение «натуральное число n делится без остатка на натуральное число m». 
Для какого наименьшего натурального числа А формула
ДЕЛ(x, A) → (¬ДЕЛ(x, 28) ∨ ДЕЛ(x, 42))
тождественно истинна (то есть принимает значение 1 при любом натуральном значении переменной х)?'''

def delka (x,a):
	if x%a==0:
		return True
	else:
		return False
for a in range (2,1001):
	k = 0
	for x in range(2,1001):
		if (delka(x,a)<=(not(delka(x,28))+delka(x,42)))==1:
			pass
		else:
			k=1
			break
	if k ==0:
		print (a)
		break

#16
'''Алгоритм вычисления значения функции F(n), где n – натуральное число, задан следующими соотношениями:
F(n) = n*n + 5*n + 4, при n > 30
F(n) = F(n+1) + 3*F(n+4), при чётных n ≤ 30
F(n) = 2*F(n+2) + F(n+5), при нечётных n ≤ 30
Определите количество натуральных значений n из отрезка [1; 1000], для которых сумма цифр значения F(n) равна 27.'''

def F (n):
	if n>30:
		return n*n + 5*n + 4
	if n<=30 and n%2==0:
		return F(n+1) + 3*F(n+4)
	if n<=30 and n%2==1:
		return 2*F(n+2) + F(n+5)

kolvo = 0
for i in range (1,1001):
	k = F(i)
	t = 0
	while k>0:
		t+=k%10
		k=k//10
	if t == 27:
		kolvo+=1
print (kolvo)

#17 
'''Рассматривается множество целых чисел, принадлежащих отрезку [1606;9680], которые делятся на 11 и 
не делятся на 7, 13, 17 и 19. Найдите количество таких чисел и максимальное из них.
 В ответе запишите два числа через пробел: сначала количество, затем максимальное число.'''
maksi = 0
kolvo = 0
for i in range (1606,9681):
	if i%11==0 and i%7!=0 and i%13!=0 and i%17!=0 and i%19!=0:
		kolvo+=1
		if maksi<i:
			maksi = i
print(kolvo,maksi)

#22
'''Укажите наименьшее пятизначное число x, при вводе которого алгоритм печатает сначала 4, а потом 2.'''
for i in range (10000,100000):
	x = i
	a = 0 
	b = 0
	while x > 0: 
	  y = x % 10
	  if y > 3: a = a + 1
	  if y < 8: b = b + 1
	  x = x // 10
	if a==4 and b==2:
		print(i)
		break

#23
'''Исполнитель Калькулятор преобразует число на экране. У исполнителя есть три команды, которым присвоены номера:
1. Прибавить 1
2. Прибавить 3
3. Умножить на 2
Программа для исполнителя Калькулятор – это последовательность команд. 
Сколько существует программ, для которых при исходном числе 1 результатом является число 15?'''
a = [0]*16
a[1]=1
for i in range (2,16):
	a[i]=a[i-1]
	if i-3>=1:
		a[i]+=a[i-3]
	if i%2==0 and i/2>=1:
		a[i]+=a[int(i/2)]
print (a[15])

#24
with open('24-j5.txt', 'r') as f:
    a = f.read().splitlines()
n = 0
for i in range (len(a)):
	for j in range (len(a[i])):
		try:
			if a[i][j]=='S' and a[i][j+1]=='O' and a[i][j+2]=='C' and a[i][j+3]=='K' and a[i][j+4]=='C'\
			and a[i][j+5]=='O' and a[i][j+6]=='S':
				n+=1
		except:
			pass
print (n)

#25
for i in range (164700, 164753):
	d = 0
	k = 0
	l = 0
	for j in range (1,int(i*.5//1)):
		if i%j==0:
			if i/j == i/(i/j):
				d+=1
				if l<(i/j):
					k=l
					l=i/j
			else:
				d+=2
				if l<(i/j):
					l=i/j
				if l<j:
					l=j
				if l>j and k<j:
					k=j
				if l>(i/j) and k<(i/j):
					k = i/j
	if d==6:
		print (int(k),int(l))


#27
n = int(input())
aa = []
summ = 0
for i in range (n):
	a,b=map(int,input().split())
	summ+=max(a,b)
	k = max(a,b) - min(a,b)
	aa.append(k)
aa.sort()
print (summ,summ%16)
for i in range (10):
	print (aa[i],' ')
#print (aa)
