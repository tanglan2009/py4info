import re
s = "From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008"
lst = re.findall('@(\S+)', s)
print lst

s2 = 'From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008'
lst2 = re.findall('\S+?@\S+', s2)
print lst2

lst3 = re.findall('\S+@\S+', s)
print lst3

# lst4 = re.findall('^From (\S+@\S+)', s)
# print lst4
# x = 'From: Using the : character'
# y = re.findall('^F.+:', x)
# print y

# Extracting a host name - using find and string slicing
data = "From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008"

# atpos = data.find('@')
# print atpos
# sppos = data.find(' ', atpos)
# print sppos
#
# host = data[atpos: sppos + 1]
# print host

words = data.split()
email = words[1]
pieces = email.split('@')
print pieces[1]

host_1 = re.findall('@([^ ]*)', data)
print host_1
host_2 = re.findall('^From .*@([^ ]*)', data)
print host_2
print host_2[0]


x = 'From: Using the : character'
y = re.findall('^F.+:', x)
print y







# hand = open('mbox-short.txt')
# for line in hand:
#     line = line.rstrip()
#     if line.find('From:') >=0:
#         print line
#
#
# import re
#
# hand = open('mbox-short.txt')
# for line in hand:
#     line = line.rstrip()
#     if re.search('From:', line):
#         print line
#
# hand