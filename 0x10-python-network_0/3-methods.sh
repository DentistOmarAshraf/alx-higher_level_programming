#!/bin/bash
# To know allowed method
curl -sI "$1" | grep "Allow" | sed 's/Allow: //g'
