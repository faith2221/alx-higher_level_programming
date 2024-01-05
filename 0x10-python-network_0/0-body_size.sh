#!/bin/bash
# Bash script that takes in a URL,sends a request and displays size of body.
curl -s "$1" | wc -c
