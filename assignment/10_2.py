


name = raw_input("Enter file:")
if len(name) < 1:
	name = 'mbox-short.txt'
handle = open(name)
d = dict()
for line in handle:
	line = line.rstrip()
 	if not line.startswith('From '): continue
 	words= line.split()
 	#print words
 	time = words[5]
 	#print type(time)
 	hour = time.split(':')[0]
 	print hour
 	
 	d[hour]= d.get(hour,0) +1

t = d.items()
#print t
#print type(t)
t.sort()
#print t
for key, val in t:
	print key, val
