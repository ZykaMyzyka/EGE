a=[]
for i in range(1512,13203):
    if i%7==0 and i%13!=0 and i%11!=0 and i%17!=0 and i%23!=0:
        a.append(i)
print(len(a),max(a))
