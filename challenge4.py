import requests
import json
import numpy as np
from json import dumps

url = 'http://challenge.code2040.org/api/prefix'

submitUrl = 'http://challenge.code2040.org/api/prefix/validate'

temp = {
	'token':'b622fb971a3ca781b60c8af66f68fe57'
	}

resp = requests.post(url, data = temp)

print (resp.text)
jsonData = resp.text
jsonToPython = json.loads(jsonData)

prefix = jsonToPython['prefix']
arrayWithOutPrefix = jsonToPython['array']
print ("-----------------")
#print arrayWithOutPrefix


for word in arrayWithOutPrefix[:]:
	if word.startswith(prefix):
		arrayWithOutPrefix.remove(word)

myArray = np.asarray(arrayWithOutPrefix)

#print myArray



postReverseString = {
	'token':'b622fb971a3ca781b60c8af66f68fe57',
	'array': arrayWithOutPrefix
	}
headers = {'Content-Type': 'application/json', 'Accept':'application/json'}
#encoded_str = json.dumps(postReverseString)
encodedArray = json.dumps(postReverseString, separators=(',', ':'))
print('-----------')
print encodedArray

resp = requests.post(submitUrl, data = encodedArray, headers = headers)
print (resp.text)

