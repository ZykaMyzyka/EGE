for d in range(1,10000):
    d = int(d)
    d1=d
    s = 0
    n = 0
    while n < 200:
      s = s + 64
      n = n + d
    if s==192:
        print(d1)
        break
