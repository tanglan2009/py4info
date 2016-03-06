import re
s1 = '<p>Please click <a href="http://www.dr-chuck.com">here</a></p>'
s2 = re.findall('href="(.+)"', s1)
print s2