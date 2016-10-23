import requests

url = 'http://challenge.code2040.org/api/reverse'

temp = {
	'token':'b622fb971a3ca781b60c8af66f68fe57'
	}

resp = requests.post(url, data = temp)


print (resp.text)
