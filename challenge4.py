import requests
import json
import numpy as np

url = 'http://challenge.code2040.org/api/prefix'

submitUrl = 'http://challenge.code2040.org/api/prefix/validate'

temp = {
	'token':'b622fb971a3ca781b60c8af66f68fe57'
	}

resp = requests.post(url, data = temp)

#print (resp.text)
jsonData = resp.text
jsonToPython = json.loads(jsonData)

prefix = jsonToPython['prefix']
arrayWithOutPrefix = jsonToPython['array']

#finalList = [prefix for prefix in array if not determine(prefix)]

print jsonToPython['array']

for word in arrayWithOutPrefix[:]:
	if word.startswith(prefix):
		arrayWithOutPrefix.remove(word)

#print prefix
#print arrayWithOutPrefix


#myArray = np.asarray(arrayWithOutPrefix)
#print myArray

#indexOfMatchingWord = array.index(jsonToPython[''])


#testing
"""
for u in jsonToPython:
	print('---------------')
	print jsonToPython[u]

print(jsonToPython['haystack'])
"""
encoded_str = json.dumps(arrayWithOutPrefix)
headers = {'content-type': 'application/json'}
tok = 'b622fb971a3ca781b60c8af66f68fe57'
postReverseString = {
	'token': tok,
	'array': arrayWithOutPrefix
	}

print('-----------')
print postReverseString

resp = requests.post(submitUrl, data = json.dumps(postReverseString))
print (resp.text)

