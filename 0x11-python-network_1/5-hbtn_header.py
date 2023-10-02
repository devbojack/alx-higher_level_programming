#!/usr/bin/python3
"""
 Takes in a URL
 Sends a request to the URL and
 Displays the variable value X-Request-Id in the response header
"""

import requests
import sys

if __name__ == '__main__':
    url = sys.argv[1]

    r = requests.get(url)
    print(r.headers.get('X-Request-Id'))
