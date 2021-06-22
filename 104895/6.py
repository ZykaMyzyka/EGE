for i in range (1000):
  s = i
  n = 1
  while s < 200:
    s = s + 25
    n = n * 2
  if n==64:
    print (i)