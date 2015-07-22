import operator
fh = open('mbox-short.txt')
d = dict()
for line in fh:
	line = line.rstrip()
	
	if line == '': continue
	if not line.startswith('From '): continue
	words = line.split()
	if words[1] not in d:
		d[words[1]] = 1
	else: 
		d[words[1]] = d[words[1]] + 1
vals = d.values()
print max(d.iteritems(), key=operator.itemgetter(1))[0], max(vals)
