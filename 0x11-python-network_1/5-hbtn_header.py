#!/usr/bin/python3
"""
Display X-Request-Id from body response using requests lib
"""

import sys
import requests

if __name__ == "__main__":
	res = requests.get(sys.argv[1])
	print(res.headers.get("X-Request-Id"))
