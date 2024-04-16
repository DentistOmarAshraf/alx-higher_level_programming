#!/usr/bin/python3
"""
Post request using requests lib
"""


if __name__ == "__main__":
    """
    POST req
    """
    import sys
    import requests

    srch = sys.argv[1]
    url = "http://0.0.0.0:5000/search_user"
    dt = {"q": sys.argv[1]}
    res = requests.post(url, data=dt)
    print(res.text)
