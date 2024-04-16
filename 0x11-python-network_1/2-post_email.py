#!/usr/bin/python3
"""
Send POST request to server
"""


if __name__ == "__main__":
    """
    Send POST req
    """

    import sys
    from urllib.request import urlopen, Request
    from urllib.parse import urlencode

    url = sys.argv[1]
    mail = sys.argv[2]
    dt = {"email": mail}
    dt = urlencode(dt)
    dt = dt.encode("ascii")

    req = Request(url, method="POST", data=dt)

    with urlopen(req) as f:
        print(f.read().decode("utf-8"))
