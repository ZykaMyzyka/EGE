a=[]
for i in range(1100,11001):
    if i%6==0 and i%7!=0 and i%13!=0 and i%17!=0 and i%23!=0:
        a.append(i)
print(len(a),max(a))
