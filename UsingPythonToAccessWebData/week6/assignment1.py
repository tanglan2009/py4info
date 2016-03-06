import urllib, json

url = '  http://python-data.dr-chuck.net/comments_188707.json?'

address = raw_input('Enter location: ')
print 'Retrieving', url
uh = urllib.urlopen(url)
data = uh.read()
print 'Retrieved',len(data), 'character'

try: js = json.loads(str(data))
except: js = None

sum = 0
for item in js['comments']:
    sum += item['count']

print sum

