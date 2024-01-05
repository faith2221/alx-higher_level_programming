#!/bin/bash
# A URL as an argument, sends a GET request to the URL, and displays the body
curl -sH "X-School-User-Id: 98" "$1"
