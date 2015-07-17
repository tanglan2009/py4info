
word = 'brontosaurus'
d = dict()
for c in word:
	if c not in d:
		d[c] = 1
	else:
		d[c] +=1
print d

# Improve the above code by using get method.

word = 'brontosaurus'
d = dict()
for c in word:
	d[c] = d.get(c,0) + 1
print d