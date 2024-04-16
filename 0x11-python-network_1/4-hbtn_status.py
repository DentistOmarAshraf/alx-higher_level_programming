#!/usr/bin/python3
"""
Fetch Using requests lib
"""


if __name__ == "__main__":
    """
    requests lib
    """
    import requests
    res = requests.get("https://alx-intranet.hbtn.io/status")
    print("Body response:")
    print("\t- type: {}".format(type(res.text)))
    print("\t- content: {}".format(res.text))
