import requests

# Code 2040 challenge #3 Reverse String
# Author: Doanh Tran(Tochi)

url = 'http://challenge.code2040.org/api/reverse'

submitUrl = 'http://challenge.code2040.org/api/reverse/validate'

temp = {
	'token':'key'
	}
#make request to get the string from the server
resp = requests.post(url, data = temp)
#revers string
stringReverse = resp.text[::-1];

postReverseString = {
	'token':'key',
	'string': stringReverse
	}
#submit the string
resp = requests.post(submitUrl, data = postReverseString)

