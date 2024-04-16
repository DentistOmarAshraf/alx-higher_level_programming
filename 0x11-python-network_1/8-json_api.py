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
    
    if len(sys.argv) > 1:
        srch = sys.argv[1]
    else:
        srch = ""
    url = "http://0.0.0.0:5000/search_user"
    dt = {"q": srch}
    res = requests.post(url, data=dt)
    print(res.text)
