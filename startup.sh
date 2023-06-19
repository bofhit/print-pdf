#!/bin/bash

# Start CUPs service
service cups start 

# Run flask app
python3 app/app.py
