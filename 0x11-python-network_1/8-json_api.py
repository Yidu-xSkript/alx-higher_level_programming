#!/usr/bin/python3
"""
query search
response in json
print id & name if json not empty
"""

import sys
import requests

if __name__ == "__main__":
	query = "" if len(sys.argv) == 1 else sys.argv[1]
	payload = {"q": query}
	res = requests.post("http://0.0.0.0:5000/search_user", data=payload)

	try:
		json_res = res.json()
		if json_res == {}:
			print("No Result")
		else:
			print("[{}] {}".format(json_res.get("id"), json_res.get("name")))
	except ValueError:
		print("Not a valid JSON")
