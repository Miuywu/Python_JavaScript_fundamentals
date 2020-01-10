#!/bin/bash
# curl and display all http methods
curl -s "$1" | grep Allow | cut -cd' ' -f1
