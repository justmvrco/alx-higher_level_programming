#!/bin/bash
# script to display all allowed http methods of a URL
curl -sI "$1" | grep Allow | cut -d " " -f 2-
