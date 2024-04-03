#!/bin/bash
# Bring Content-Length header

curl -s -I "$1" | grep "Content-Length" | sed 's/[^0-9]*//g'
