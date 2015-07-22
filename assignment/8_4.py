fh = open('romeo.txt')
lst = list()
for line in fh:
	line = line.rstrip()
	words = line.split()
	
	for word in words:
		if word not in lst:
			#lst = lst + [word] 
			 lst.append(word)
lst.sort()
print lst
	