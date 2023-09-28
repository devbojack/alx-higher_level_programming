#!/bin/bash
# Takes in a URL
# Sends a request to that URL
# And displays the size of the body of the response
curl -sI "$1" | grep "Content-Length" | cut -d' ' -f2
