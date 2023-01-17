#!/usr/bin/python3
"""
takes url,
display body response
using requests lib
"""

import sys
import requests

if __name__ == "__main__":
	res = requests.get(sys.argv[1])
	if res.status_code >= 400:
		print("Error Code: {}".format(res.status_code))
	else:
		print(res.text)
