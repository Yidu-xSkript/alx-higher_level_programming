#!/usr/bin/python3
"""
Script that
- takes in URL & email
- sends a POST request with the email parameter
- displays the body response (utf-8)
"""

import sys
import urllib.parse
import urllib.request

if __name__ == "__main__":
	url = sys.argv[1]
	payload = urllib.parse.urlencode({"email": sys.argv[2]}).encode('ascii')
	request = urllib.request.Request(url, payload)

	with urllib.request.urlopen(request) as res:
		print(res.read().decode('utf-8'))
