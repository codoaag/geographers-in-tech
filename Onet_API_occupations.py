# Purpose:  Read data from the O*NET API - occupations
# Author:   Coline Dony
# Date:     Sept 21, 2017

import urllib2
import xml.etree.ElementTree
from make_dict_from_tree import make_dict_from_tree

# The URL with your API request
# The response will be in an XML format
url_api_request = urllib2.Request('https://services.onetcenter.org/ws/online/search?keyword=geography')
url_api_request.add_header('Authorization', 'Basic YW1lcmljYW5fYXNzb2NpYXRpb246MjQyM2VtZw==')

# The API request is sent using the internet
# The XML response is then read as a string
api_response_string = urllib2.urlopen(url_api_request).read()

# The XML response string is now converted
# The response is now in a dictionary format
api_response = make_dict_from_tree(xml.etree.ElementTree.fromstring(api_response_string))

for occupation in api_response['occupations']['occupation']:
    print occupation['code'], occupation['title']
