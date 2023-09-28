#!/bin/bash
# Takes in a URL and displays all HTTP methods the server will accept
curl -sI "$1" -X OPTION | grep "Allow:" | cut -d':' -f2 | sed 's/ //'
