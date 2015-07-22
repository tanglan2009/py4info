fname = raw_input('Enter a file name: ')
if len(fname) < 1:
    fname = 'mbox-short.txt'
fh = open(fname)
d = dict()
for line in fh:
    line = line.rstrip()
    if not line.startswith('From '): continue
    words = line.split()
    emailAddress = words[1]
    d[emailAddress] = d.get(emailAddress,0) + 1
print d
