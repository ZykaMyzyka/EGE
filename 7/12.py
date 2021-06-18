a='1'*2019+'2'*2119
while  '222' in a:
    a=a.replace('222','1',1)
    a=a.replace('111','2',1)
print(a)
