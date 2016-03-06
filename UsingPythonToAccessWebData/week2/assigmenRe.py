import re
hand = open('regex_sum_188701.txt')
sum = 0
for line in hand:
    line = line.rstrip()
    lst = re.findall('[0-9]+', line)
    if len(lst) >=1:
        numlst = lst
        for num in numlst:
            sum += int(num)
print sum