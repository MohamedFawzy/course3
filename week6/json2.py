import json
input = '''
[
    {
        "id":"1",
        "name":"test"
    },
    {
        "id":"2",
        "name":"test2"
    }

]'''

info = json.loads(input)
print 'User counts:', len(info)

for item in info:
    print 'Name:', item["name"]
    print "Id:", item["id"]
