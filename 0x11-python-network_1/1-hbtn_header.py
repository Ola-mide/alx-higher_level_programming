#!/usr/bin/python3
"""
A module that takes in a URL and sends a request to it in order to
display the value of the X-Request-Id variable found in the header
of the response
"""
import sys
import urllib.request


if __name__ == "__main__":
    with urllib.request.urlopen(sys.argv[1]) as r:
        print(r.headers.get('X-Request-Id'))
