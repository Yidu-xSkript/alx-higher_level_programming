#!/bin/bash
# displays body size of http response
curl -sI "$1" | grep 'Content-Length' | sed 's/^Content-Length: //'
