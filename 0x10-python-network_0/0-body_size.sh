#!/bin/bash
# a bash script that displays the size of the body of the response
curl -sI "$1" | awk -v FS=": " '/^Content-Length/{print $2}'
