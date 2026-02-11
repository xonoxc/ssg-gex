#!/usr/bin/bash

python3 src/main.py
echo "Starting up the server...."
cd public && python3 -m http.server 8888

