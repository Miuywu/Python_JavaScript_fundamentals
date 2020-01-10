#!/bin/bash
# displays status code of response
curl -so /dev/null --head -w "%{http_code}" "$1"
