for s in range(1,100000):
    s1 = s
    n = 5
    while n > 0:
      s = s + n
      n = n - 1
    if s<=550:
        print(s1)
