import urllib
import json

serviceUrl = 'http://maps.googleapis.com/maps/api/geocode/json?'
while True:
    address = raw_input("Enter location: ")
    if len(address) < 1 : break

    url = serviceUrl + urllib.urlencode({'sensor':'false','address':address})
    print 'Reteriving', url
    uh = urllib.urlopen(url)
    data = uh.read()
    print 'Retreived', len(data), 'characters'

    try:
        js = json.loads(str(data))
    except:
        js = None
    if 'status' not in js or js['status'] != 'OK':
        print '===== Failure To Retrive ====='
        print data
        continue
    print json.dumps(js, indent=4)
    lat = js['results'][0]['geometry']['location']['lat']
    lng = js['results'][0]['geometry']['location']['lng']

    print 'lat:', lat, 'lng:', lng

    location = js['results'][0]['formatted_address']
    print location
