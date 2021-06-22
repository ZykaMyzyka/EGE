s = '>1111111111111111111122222222222222222222222223333333333333333333333333333333333333333'
while '>1' in s or '>2' in s or '>3' in s:
 	if '>1' in s:
 		s = s.replace ('>1','22>',1)
 	elif '>1' in s:
 		s = s.replace ('>2','2>1',1)
 	elif '>1' in s:
 		s = s.replace ('>3','1>2',1)
n = 0
for i in range (len(s)):
	if s[i]=='1' or s[i]=='2' or s[i]=='3':
		n+=int (s[i])