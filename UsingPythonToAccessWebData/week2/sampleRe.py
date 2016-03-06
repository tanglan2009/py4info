import re

hand = open('regex_sum_42.txt')
total = 0
for line in hand:
    line = line.strip()
    lst = re.findall('[0-9]+', line)
    if len(lst)>=1:
        numlist = lst
        #print numlist
        for num in numlist:
            print num
        total += int(num)
print total

