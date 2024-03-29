#!/usr/bin/python3
"""
takes a url,
displays value of X-Request-Id variable
found in the header of the response.
"""

import sys
import urllib.request

if __name__ == "__main__":
	url = sys.argv[1]

	with urllib.request.urlopen(url) as res:
		print(dict(res.headers).get("X-Request-Id"))
