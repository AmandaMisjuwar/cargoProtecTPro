import urllib.request
import json

body = {'name': "Amanda", 'conf': 0.77, 'bodies': 2}

myurl = "http://pmoe7.com"  # http://pmoe7.com
req = urllib.request.Request(myurl)
req.add_header('Content-Type', 'application/json; charset=utf-8')
jsondata = json.dumps(body)
jsondataasbytes = jsondata.encode('utf-8')  # needs to be bytes
req.add_header('Content-Length', len(jsondataasbytes))
print(jsondataasbytes)
response = urllib.request.urlopen(req, jsondataasbytes)
