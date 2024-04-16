#!/usr/bin/python3
"""
Fetching Using requests lib
"""


if __name__ == "__main__":
    """
    Fetchin using requests lib
    """
    import sys
    import requests

    res = requests.get(sys.argv[1])
    try:
        print(res.headers["X-Request-Id"])
    except KeyError as e:
        pass
