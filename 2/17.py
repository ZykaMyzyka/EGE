a=[]
for i in range(1033,7737):
    if i%5==0 and i%11!=0 and i%17!=0 and i%19!=0 and i%23!=0:
        a.append(i)
print(len(a))
print(max(a))
