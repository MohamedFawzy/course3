import json
import urllib
json_url = raw_input("Enter location: ")
print 'Retriveing', json_url
data = urllib.urlopen(json_url).read().decode('UTF-8')
print 'Retrieved', len(data), 'characters'
json_object = json.loads(data)
sum=0
total_numbers=0

for comments in json_object['comments']:
    sum += int(comments['count'])
    total_numbers+=1

print 'Count:', total_numbers
print 'Sum:', sum
