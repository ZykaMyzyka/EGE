n=0
for x in range(1,10000):
    x1=x
    
    x = int(x)
    a = 0 
    b = 0
    while x > 0: 
      a = a + 1
      b = b + (x % 10)
      x = x // 10
    if a==2 and b==12:
        n+=1
print(n)
