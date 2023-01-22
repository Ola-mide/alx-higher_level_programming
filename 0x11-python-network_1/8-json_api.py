#!/usr/bin/python3
"""
A module that sends a POST request
"""
import requests
import sys


if __name__ == "__main__":
    data = {
            "q": sys.argv[1] if len(sys.argv) > 1 else ""
            }
    response = requests.post("http://0.0.0.0:5000/search_user", data=data)
    try:
        if not response.json():
            print("No result")
        else:
            print("[{}] {}".format(
                response.json().get("id"),
                response.json().get("name")
                ))
    except ValueError:
        print("Not a valid JSON")
