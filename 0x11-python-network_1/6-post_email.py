#!/usr/bin/python3
"""
requests lib
"""


if __name__ == "__main__":
    """
    requests lib
    """
    import sys
    import requests

    dt = {"email": sys.argv[2]}
    res = requests.post(sys.argv[1], data=dt)
    print(res.text)
