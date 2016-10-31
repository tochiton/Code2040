import requests
import json
import numpy as np
import datetime
from datetime import datetime, timedelta
from dateutil import parser
import dateutil.parser as dp

# Code 2040 challenge #4 Reverse String
# Author: Doanh Tran(Tochi

url = 'http://challenge.code2040.org/api/dating'

submitUrl = 'http://challenge.code2040.org/api/dating/validate'

temp = {
	'token':'key'
	}

resp = requests.post(url, data = temp)

jsonData = resp.text
jsonToPython = json.loads(jsonData)
# get the data from the Json object
datestamp = jsonToPython['datestamp']
interval = jsonToPython['interval']

# parse the string in the following format
parsed_t = dp.parse(datestamp)
t_in_seconds = parsed_t.strftime('%s')
totaSeconds = int(t_in_seconds) + int(interval)

date_object = datetime.strptime(datestamp, '%Y-%m-%dT%H:%M:%SZ')

add = date_object + timedelta(seconds = int(interval))

addedtime = str(add)

temptime = addedtime + "Z"

another = temptime.replace(" ", 'T')

headers = {'content-type': 'application/json'}

postReverseString = {
	'token':'key',
	'datestamp': another
	}

resp = requests.post(submitUrl, data = postReverseString)
print (resp.text)

