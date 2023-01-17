#!/usr/bin/python3
"""
List 10 commits from a Github repo.
use https://api.github.com/repos/OWNER/REPO/commits
1st arg - repo
2nd arg - owner
using the requests lib
"""
import sys
import requests

if __name__ == "__main__":
	url = "https://api.github.com/repos/{}/{}/commits".format(
		sys.argv[2], sys.argv[1])
	response = requests.get(url)
	commit = response.json()

	try:
		for i in range(10):
			print("{}: {}".format(
				commit[i].get("sha"),
				commit[i].get("commit").get("author").get("name")))
	except IndexError:
		pass
