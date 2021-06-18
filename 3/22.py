for x in range(1,10000):
    x1=x
    x=int(x)
    L = 0 
    M = 0
    while x > 0 : 
      L = L+1
      if M < (x % 10): 
        M = x % 10
      x = x // 10
    if L==3 and M==7:
        print(x1)
