#!/usr/bin/python3
"""
A module that sends a request to a URL and displays the value of the variable
X-Request-Id
"""
import sys
import requests


if __name__ == "__main__":
    response = requests.get(sys.argv[1])
    print(response.headers.get("X-Request-Id"))
