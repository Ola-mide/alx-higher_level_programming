#!/usr/bin/bash
# a bash script that sends a post request
curl "$1" -sX POST -d "email=test@gmail.com" -d "subject=I will always be here for PLD"
