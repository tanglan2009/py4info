import urllib, json


serviceurl = 'http://python-data.dr-chuck.net/geojson?'

while True:
    address = raw_input('Enter location:')
    if len(address) < 1: break

    url = serviceurl + urllib.urlencode({'sensor' : 'false', 'address' : address})
    print 'Retrieving', url
    uh = urllib.urlopen(url)
    data = uh.read()
    print 'Retrieved', len(data), 'characters'

    js = json.loads(str(data))
    print "Place id", js["results"][0]["place_id"]
    #print js['Place_id']


