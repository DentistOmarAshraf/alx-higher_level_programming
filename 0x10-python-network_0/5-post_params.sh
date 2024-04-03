#!/bin/bash
# Send POST request
curl -H 'email:test@gmail.com' -H 'subject:I will always be here for PLD' -sX POST "$1"
