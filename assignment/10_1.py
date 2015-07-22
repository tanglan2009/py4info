fname = raw_input('Enter a file name: ')
fh = open(fname)
d = dict()
for line in fh:
    line = line.rstrip()
    if not line.startswith('From '): continue
    words = line.split()
    # print words[1]
    d[words[1]] = d.get(words[1], 0) + 1
t = d.items()
ls = list()
for email, cou in t:
    ls.append((cou, email))

ls.sort(reverse=True)
for cou, email in ls[0:1]:
    print email, cou