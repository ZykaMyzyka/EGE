'''Число 572 записали в системах счисления с основаниями от 2 до 10 включительно
. При каких основаниях в записи этого числа есть две одинаковые цифры
, стоящие рядом? В ответе укажите сумму всех подходящих оснований.'''

for i in range (2,10):
	k = 572
	a = []
	while k>0:
		a.append(k%i)
		k=k//i
	print (a)