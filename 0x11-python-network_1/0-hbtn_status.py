#!/usr/bin/python3
"""
Making Request using urllib module
"""


if __name__ == "__main__":
    """
    Making Request using urllib module
    """
    from urllib.request import urlopen

    with urlopen("https://alx-intranet.hbtn.io/status") as f:
        x = f.read()
        print("Body response:")
        print("\t- type: {}".format(type(x)))
        print("\t- content: {}".format(x))
        print("\t- utf8 content: {}".format(x.decode("utf-8")))
