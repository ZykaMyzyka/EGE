import itertools
a=list(itertools.permutations('МАГИСТР', r=5))
count=0
for i in a:
    if (i.count('А')<=1 and i.count('И')==0) or (i.count('А')==0 and i.count('И')<=1):
        count+=1
print(count)
    
    
