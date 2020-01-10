#!/bin/bash
# curl and display all http methods
curl --silent --head "$1" | grep Allow | cut --complement -d' ' -f1
