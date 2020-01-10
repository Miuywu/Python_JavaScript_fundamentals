#!/bin/bash
# cURL and display size of response
curl -s "$1" | wc -c
