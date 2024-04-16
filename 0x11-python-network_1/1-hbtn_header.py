#!/usr/bin/python3
"""
Making Request using urllib module and know some response headers
"""


if __name__ == "__main__":
    """
    Making Request and read response headers
    """
    import sys
    from urllib.request import urlopen

    with urlopen(sys.argv[1]) as f:
        print(f.headers["X-Request-Id"])
