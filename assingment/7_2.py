fh = open ('mbox-short.txt')
count = 0
sum = 0
for line in fh:
	if line.startswith('X-DSPAM-Confidence:'):
		line = line.strip()
		abc = line.find(':')
		bcd = line[abc + 1:]
		bcd = float(bcd)
		
		count += 1
		sum = sum + bcd
		

print count, sum/count
	
