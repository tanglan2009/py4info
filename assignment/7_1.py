
fhand = open('words.txt')
inp = fhand.read()
for line in fhand:
    line = line.rstrip()
print inp.upper()


	
	