a=[]
for i in range(200,9121):
    if i%8==0 and i%7!=0 and i%11!=0 and i%17!=0 and i%19!=0:
        a.append(i)
print(len(a),min(a))
