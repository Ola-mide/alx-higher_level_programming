#!/usr/bin/python3
"""
A module that fetches a specific url - https://alx-intranet.hbtn.io/status
"""
import urllib.request


if __name__ == "__main__":
    request = urllib.request.Request('https://alx-intranet.hbtn.io/status')
    with urllib.request.urlopen(request) as response:
        page = response.read()
    print("Body response:")
    print("\t- type: {}".format(type(page)))
    print("\t- content: {}".format(page))
    print("\t- utf8 content: {}".format(page.decode('utf-8')))
