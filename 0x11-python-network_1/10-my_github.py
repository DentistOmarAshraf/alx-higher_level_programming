#!/usr/bin/python3
"""
GitHub API
"""


if __name__ == "__main__":
    """
    GitHub APT
    """
    import sys
    import requests

    user = sys.argv[1]
    pswd = sys.argv[2]
    pswd = "Bearer " + pswd

    head = {"Authorization": pswd,
            "Accept": "application/vnd.github+json",
            "X-GitHub-Api-Version": "2022-11-28"}

    url = "https://api.github.com/user"

    res = requests.get(url, headers=head)

    user_data = res.json()

    if "id" in user_data.keys() and user_data["login"] == user:
        print(user_data["id"])
    else:
        print("None")
