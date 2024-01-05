#!/bin/bash
# Makes akes a request to 0.0.0.0:5000/catch_me
# Causes server to respond with message containing You got me!, in body response.
CURL -sL -X PUT -H "Origin:HolbertonSchool" -d "user_id=98" 0.0.0.0:5000/catch_me
