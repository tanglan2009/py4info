import string
fname = 'Romeo-Longer.txt'
fhand = open(fname)

counts = dict()
for line in fhand:

    line = line.strip().lower()
    line = line.translate(None, string.punctuation + ' ')
    print line

    # ls1 = list(line)
    # print ls1
    for letter in line:
        counts[letter] = counts.get(letter, 0) + 1
print counts

#Sort the dictionary by value
ls = list()
for letter, cou in counts.items():
    ls.append((cou, letter))
ls.sort(reverse=True)

for cou, letter in ls:
    print letter,cou