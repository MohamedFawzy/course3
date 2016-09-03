import urllib
import json

serviceUrl = "http://python-data.dr-chuck.net/geojson?"

address = raw_input("Enter location: ")
params = {"sensor":"false", "address": address}

url = serviceUrl+urllib.urlencode(params)
print 'Reteriveing', url
data = urllib.urlopen(url).read().decode('UTF-8')
print 'Retreiving', len(data), 'characters'
json_object = json.loads(data)

place_id = json_object['results'][0]['place_id']
print 'place_id', place_id
