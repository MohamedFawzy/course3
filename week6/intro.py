import json
data = '''{
    "name":"mohamed",
    "phone":{
        "type":"int1",
        "number":"+21233123123"
    },
    "email":{
        "hide":"yes"
    }
}'''

info = json.loads(data)
print 'Name:', info["name"]
print 'Hide:', info["email"]["hide"]
