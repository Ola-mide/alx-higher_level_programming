#!/usr/bin/python3
"""
A module that takes in a URL and an email and sends a POST request to the
passed URL with the email as a parameter and displays the body of the response
decoded in utf-8
"""
import sys
from urllib import request, parse


if __name__ == "__main__":
    data = parse.urlencode({"email": sys.argv[2]}).encode()
    with request.urlopen(sys.argv[1], data) as response:
        body = response.read()
    print(body.decode('utf8'))
