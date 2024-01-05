#!/bin/bash
# Sends  JSON POST request to a URL passed as the first argument, display body
curl -s H "Content-Type: application/json" -d "$(cat "$2")" "$1"
