#!/usr/bin/python3
"""Sends a request to the URL and displays value of X-Request-Id variable"""
import sys
import requests


if __name__ == "__mian__":
    url = sys.argv[1]
    r = requests.get(url)
    print(r.headers.get("X-Request-Id"))
