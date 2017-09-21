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
url_api_request = 'http://api.datausa.io/api/?show=geo&required=diabetes&sumlevel=all&geo=31000US14460'

# The API request is sent using the internet
# The JSON response is then read as a string
api_response_string = urllib2.urlopen(url_api_request).read()

# The JSON response string is now converted
# The response is now in a dictionary format
api_response = json.loads(api_response_string)
