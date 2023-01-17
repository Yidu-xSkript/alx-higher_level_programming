#!/usr/bin/python3
"""
POST request using requests lib
send email parameter to url
"""

import requests
import sys


if __name__ == "__main__":
	response = requests.post(sys.argv[1], data={'email': sys.argv[2]})
	print(response.text)
