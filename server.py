import requests

url = 'http://challenge.code2040.org/api/reverse'

submitUrl = 'http://challenge.code2040.org/api/reverse/validate'

temp = {
	'token':'b622fb971a3ca781b60c8af66f68fe57'
	}

resp = requests.post(url, data = temp)

stringReverse = resp.text[::-1];
print (resp.text)

postReverseString = {
	'token':'b622fb971a3ca781b60c8af66f68fe57',
	'string': stringReverse
	}
resp = requests.post(submitUrl, data = postReverseString)

print (resp.text)
