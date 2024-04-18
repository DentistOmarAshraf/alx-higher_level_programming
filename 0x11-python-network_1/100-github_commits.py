#!/usr/bin/python3
"""
list GitHub Repo Commits
"""

if __name__ == "__main__":
    import sys
    import requests

    repo = sys.argv[1]
    owner = sys.argv[2]
    passwd = ""
    head = {"Accept": "application/vnd.github+json",
            "Authorization": f"Bearer {passwd}",
            "X-GitHub-Api-Version": "2022-11-28"}

    url = f"http://api.github.com/repos/{owner}/{repo}/commits"

    res = requests.get(url, head)
    data = res.json()

    y = 0
    for x in data:
        print("{}: {}".format(x["sha"], x["commit"]["author"]["name"]))
        y += 1
        if y == 10:
            break
