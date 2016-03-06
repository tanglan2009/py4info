import urllib
import xml.etree.ElementTree as ET

serviceurl = ' http://python-data.dr-chuck.net/comments_188703.xml '

while True:
    address = raw_input('Enter location: ')
    if len(address) < 1 : break

    print 'Retrieving', serviceurl
    uh = urllib.urlopen(serviceurl)
    data = uh.read()
    print 'Retrieved',len(data),'characters'
    print data
    tree = ET.fromstring(data)

# comments = tree.findall('.//comment')
#     sum = 0
#     for comment in comments:
#         count = int(comment.find('count').text)
#         sum += count
#     print sum


    counts= tree.findall('.//count')
    sum = 0
    for count in counts:
        sum += int(count.text)
    print sum