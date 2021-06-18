for s in range(1,100000):
    s1=s
    n = 0
    while 400 < s*s:
      s = s - 1
      n = n + 3
    if n<1000:
        print(s1)
