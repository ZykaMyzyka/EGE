for s in range(1,1000):
    s1 = s
    n = 1
    while n < 21:
      s = s - 1
      n = n + 2
    if s>600:
        print(s1)
        break
