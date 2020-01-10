#!/bin/bash
# email with faux body
curl -sX POST --data "email=hr@holbertonschool.com" --data "subject=I will always be here for PLD" "$1"
