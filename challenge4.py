import requests
import json
import numpy as np

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
#print arrayWithOutPrefix
print ("-----------------")

#finalList = [prefix for prefix in array if not determine(prefix)]

#print jsonToPython['array']

for word in arrayWithOutPrefix[:]:
	if word.startswith(prefix):
		arrayWithOutPrefix.remove(word)

myArray = np.asarray(arrayWithOutPrefix)

encodedArray = json.dumps(myArray)

 
postReverseString = {
	"token":"b622fb971a3ca781b60c8af66f68fe57",
	"array": myArray
	}

#encoded_str = json.dumps(postReverseString)

print('-----------')
print postReverseString

resp = requests.post(submitUrl, data= json.dumps(postReverseString))
print (resp.text)

