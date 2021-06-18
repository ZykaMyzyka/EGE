for x in range(1,10000):
    x = int(x)
    x1=x
    L = 0 
    M = 1
    while x > 0 : 
      L = L+1
      M = M*(x % 8)
      x = x // 8
    if L==3 and M==120:
        print(x1)
