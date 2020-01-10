#!/bin/bash
# cURL and display size of response
curl --silent "$1" | wc -c
