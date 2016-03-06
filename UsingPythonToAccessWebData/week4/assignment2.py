# Note - this code must run in Python 2.x and you must download
# http://www.pythonlearn.com/code/BeautifulSoup.py
# Into the same folder as this program

import urllib
from BeautifulSoup import *
url = raw_input('Enter - ')
time = 0
# while time < 7:
#     html = urllib.urlopen(url).read()
#     soup = BeautifulSoup(html)
#     # Retrieve all of the anchor tags
#     tags = soup('a')
#     tagCount = 0
#     for tag in tags:
#         tagCount += 1
#         if tagCount == 18:
#             newurl = tag.get('href', None)
#             url = newurl
#     url = newurl
#     time += 1
#     print newurl

##sample
while time < 4:
    html = urllib.urlopen(url).read()
    soup = BeautifulSoup(html)
    # Retrieve all of the anchor tags
    tags = soup('a')
    tagCount = 0
    for tag in tags:
        print tag
        tagCount += 1
        if tagCount == 3:
            newurl = tag.get('href', None)
            url = newurl
    url = newurl
    time += 1
    print newurl



