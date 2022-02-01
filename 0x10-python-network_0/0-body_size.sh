#!/bin/bash
# script to display response size for URL passed to script
curl -s -w %{size_download}"\n" "$1" -o /dev/null
