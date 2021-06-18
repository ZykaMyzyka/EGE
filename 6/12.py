a='1'*2019+'3'*2119
while '11' in a:
    a=a.replace('11','2',1)
    a=a.replace('22','3',1)
    a=a.replace('33','1',1)
print(a)
