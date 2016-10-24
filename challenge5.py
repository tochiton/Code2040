import requests
import json
import numpy as np

url = 'http://challenge.code2040.org/api/dating'

submitUrl = 'http://challenge.code2040.org/api/prefix/validate'

temp = {
	'token':'b622fb971a3ca781b60c8af66f68fe57'
	}

resp = requests.post(url, data = temp)

print (resp.text)
jsonData = resp.text
jsonToPython = json.loads(jsonData)

datestamp = jsonToPython['datestamp']
interval = jsonToPython['interval']

#finalList = [prefix for prefix in array if not determine(prefix)]

print('----------------')

print datestamp
print interval

#testing
"""
encoded_str = json.dumps(arrayWithOutPrefix)
headers = {'content-type': 'application/json'}

postReverseString = {
	'token':'b622fb971a3ca781b60c8af66f68fe57',
	'array': arrayWithOutPrefix
	}

print('-----------')
print postReverseString

resp = requests.post(submitUrl, data = json.dumps(postReverseString))
print (resp.text)
"""
