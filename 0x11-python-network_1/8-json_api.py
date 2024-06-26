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
    import json

    if len(sys.argv) > 1:
        srch = sys.argv[1]
    else:
        srch = ""
    url = "http://0.0.0.0:5000/search_user"
    dt = {"q": srch}
    res = requests.post(url, data=dt)
    try:
        data = res.text
        data = json.loads(data)
        if "id" in data.keys():
            print("[{}] {}".format(data["id"], data["name"]))
        else:
            print("No result")
    except json.decoder.JSONDecodeError as e:
        print("Not a valid JSON")
