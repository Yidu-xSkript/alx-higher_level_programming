#!/usr/bin/python3
"""
takes in url,
sends a request,
display body response
"""

import sys
import urllib.request
import urllib.error

if __name__ == "__main__":
	try:
		with urllib.request.urlopen(sys.argv[1]) as res:
			print(res.read().decode('UTF-8'))
	except urllib.error.HTTPError as error:
		print('Error code:', error.code)
