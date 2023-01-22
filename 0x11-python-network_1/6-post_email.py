#!/usr/bin/python3
"""
A module that uses the requests module to send a post request
"""
import sys
import requests


if __name__ == "__main__":
    data = {"email": sys.argv[2]}
    x = requests.post(sys.argv[1], json=data)
    print(x.text)
