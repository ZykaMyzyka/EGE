for s in range(1,10000):
    s1=s
    s=int(s)
    n = 50
    while s > 0:
      s = s // 2
      n = n - 3
    if n==23:
        print(s1)
        break
