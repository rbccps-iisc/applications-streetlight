import json
import urllib2


brokerJson = {}
brokerJsonString = ''


req = urllib2.Request('https://smartcity.rbccps.org/api/0.1.0/update')
req.add_header('Content-Type', 'application/json')
req.add_header('apikey', 'c8d57150220f44468414368697531b08')


brokerJson["exchange"] = "amq.topic"  
brokerJson["key"] =  "70b3d58ff0031de5_update"
brokerJson["body"] = "blah"

headers = {"apikey": "c8d57150220f44468414368697531b08"}

brokerJsonString = json.dumps(brokerJson)

response = urllib2.urlopen(req, brokerJsonString)
print response.read()
