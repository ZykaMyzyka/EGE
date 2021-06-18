a='КАБАЛА'
b=[]
c=[]
for q in range(len(a)):
    s=a[q]
    for w in range(len(a)):
        s1=s+a[w]
        for e in range(len(a)):
            s2=s1+a[e]
            for r in range(len(a)):
                s3=s2+a[r]
                for t in range(len(a)):
                    s4=s3+a[t]
                    for y in range(len(a)):
                        s5=s4+a[y]
                        b.append(s5)
for i in range(len(b)):
    if b[i] in c:
        s=0
    else:
        c.append(b[i])
print(c)
