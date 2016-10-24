import requests
import json

url = 'http://challenge.code2040.org/api/prefix'

submitUrl = 'http://challenge.code2040.org/api/haystack/validate'

temp = {
	'token':'b622fb971a3ca781b60c8af66f68fe57'
	}

resp = requests.post(url, data = temp)

#print (resp.text)
jsonData = resp.text
jsonToPython = json.loads(jsonData)

prefix = jsonToPython['prefix']
array = jsonToPython['array']

#finalList = [prefix for prefix in array if not determine(prefix)]

print array
for array in array : array.remove(prefix)

print prefix
print array

#indexOfMatchingWord = array.index(jsonToPython[''])


#testing
"""
for u in jsonToPython:
	print('---------------')
	print jsonToPython[u]

print(jsonToPython['haystack'])
"""
"""
postReverseString = {
	'token':'b622fb971a3ca781b60c8af66f68fe57',
	'needle': indexOfMatchingWord
	}

resp = requests.post(submitUrl, data = postReverseString)

print (resp.text)
"""