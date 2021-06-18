a='1'*130
while '111' in a:
    a=a.replace('111','2',1)
    a=a.replace('222','3',1)
    a=a.replace('333','1',1)
print(a)
