#!/usr/bin/env bash
# a bash script that sends a GET request

curl "$1" -Xs GET -H "X-School-User-Id: 98"
