#!/usr/bin/bash
# a bash script that displays all http methods

curl -Is "$1" | awk -v FS=": " '/^Allow/{print $2}'
