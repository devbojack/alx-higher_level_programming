#!/bin/bash
# Makes a request to 0.0.0.0:5000/catch_me that causes the server to respond with a message containing You got me!, in the body of the response
curl -s -X PUT -H "Content-Type: application/json" -d '{"user_id": "98"}' 0.0.0.0:5000/catch_me --output /dev/null -w "You got me!"
