
fh = open('mbox-short.txt')
d = dict()
for line in fh:
	line = line.rstrip()
	
	if line == '': continue
	if not line.startswith('From '): continue
	words = line.split()
	#print words[1]
	d[words[1]] = d.get(words[1],0) +1
	
#vals = d.values()
#print max(d.iteritems(), key=operator.itemgetter(1))[0], max(vals)

maxkey = None
maxval = None
for key, val in d.items():
	if maxval == None or maxval <= val: 
		maxval =val
		maxkey = key
print maxkey, maxval	
