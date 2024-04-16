#!/usr/bin/python3
"""
Fetching Using requests lib
"""


if __name__ == "__main__":
    import sys
    import requests

    res = requests.get(sys.argv[1])
    print(res.headers["X-Request-Id"])
