#!/usr/bin/python3
"""
A module that sends a request
"""
import sys
from urllib import error, request


if __name__ == "__main__":
    try:
        with request.urlopen(sys.argv[1]) as response:
            body = response.read()
            print(body.decode("utf8"))
    except error.HTTPError as err:
        print("Error code: {}".format(e.code))
