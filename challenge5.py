import requests
import json
import numpy as np
import datetime
from datetime import datetime, timedelta
from dateutil import parser
import dateutil.parser as dp

url = 'http://challenge.code2040.org/api/dating'

submitUrl = 'http://challenge.code2040.org/api/dating/validate'

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

parsed_t = dp.parse(datestamp)
t_in_seconds = parsed_t.strftime('%s')
totaSeconds = int(t_in_seconds) + int(interval)

#finalTime = datetime.datetime.isoformat(secondsInStringFormat)

#dt = parser.parse(datestamp,'%Y-%m-%dT%H:%M:%S.%fZ')

#dt = datetime(int(datestamp))
date_object = datetime.strptime(datestamp, '%Y-%m-%dT%H:%M:%SZ')

print date_object + timedelta(seconds = int(interval))


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
