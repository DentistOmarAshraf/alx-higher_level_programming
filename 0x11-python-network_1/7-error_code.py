#!/usr/bin/python3
"""
handle Error in requests
"""


if __name__ == "__main__":
    """handle error"""
    import sys
    import requests

    url = sys.argv[1]
    res = requests.get(url)

    if res.status_code >= 400:
        print("Error code: {}".format(res.status_code))
    else:
        print(res.text)
