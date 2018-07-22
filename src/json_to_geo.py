import requests
import json

payload = {"UID":1,"Name":"a name","Longitude":"-117.3961564","Latitude":"33.9533487"}
headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}

r = requests.post('http://ps0002022.esri.com:6180/geoevent/rest/receiver/rest-json-in', data = json.dumps(payload), headers = headers)

print(r.status_code)