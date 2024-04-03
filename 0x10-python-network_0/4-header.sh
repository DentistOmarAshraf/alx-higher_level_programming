#!/bin/bash
# sending header to server using curl
curl -H 'X-School-User-Id:98' -sX GET "$1"
