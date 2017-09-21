# Purpose:  Read data from an API
# Author:   Coline Dony
# Date:     Sept 21, 2017

import urllib2
import json

# For API's that require an API key
# Assign your key as a string to this variable
api_key = '<your api key>'

# The URL with your API request
# Request the response to be in the JSON format
headers = {'Content-type': 'application/json'}
data = json.dumps({"seriesid": ['CUUR0000SA0','SUUR0000SA0'],"startyear":"2011", "endyear":"2014"})
url_api_request = requests.post('https://api.bls.gov/publicAPI/v2/timeseries/data/', data=data, headers=headers)

# The API request is sent using the internet
# The JSON response is then read as a string
# api_response_string = urllib2.urlopen(url_api_request).read()

# The JSON response string is now converted
# The response is now in a dictionary format
api_response = json.loads(url_api_request.text)
