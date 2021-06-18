for x in range(1,10000):
    x1 = x
    a = 0 
    b = 0
    while x > 0: 
      a = a + 1
      if x % 2 == 0:
        b = b + (x % 10)
      x = x // 10
    if a==3 and b==18:
        print(x1)
        break
