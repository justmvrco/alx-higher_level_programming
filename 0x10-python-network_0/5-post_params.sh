#!/bin/bash
# script that sends a DELETE request to the URL passed and display body of response
curl -s -X "POST" "$1" -d "email=hr@holbertonschool.com&subject=I will always be here for PLD"
