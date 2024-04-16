#!/usr/bin/python3
"""
Handle HTTPError
"""


if __name__ == "__main__":
    """
    Handle HTTPError
    """
    from urllib.request import urlopen
    from urllib.error import HTTPError
    import sys

    try:
        with urlopen(sys.argv[1]) as res:
            print(res.read().decode("utf-8"))
    except HTTPError as e:
        print(e.code)
