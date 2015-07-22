'''
sort the dictionary 1)by key;
					2)by value.
'''

d = {'a': 10, 'e': 15, 'b':23, 'f': 4, 'd':8}
t = d.items()
#print d.items().sort() # output is None! WHY?
t.sort()
print t

t1 = list()
for key, val in t:
	t1.append((val, key))
t1.sort()
print t1
print 'more stuff'