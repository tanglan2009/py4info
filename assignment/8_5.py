
fh = open ('mbox-short.txt')
count = 0
for line in fh:
	
	line = line.rstrip() 
	# or here if line == '': continue
	words = line.split()
	
	if len(words) == 0: continue   # or words ==[]:
	if words[0] != 'From': continue
	print words[1]
	count += 1
print"There were %d lines in the file with From as the first word" %(count)