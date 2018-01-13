#!/bin/bash

# Start Gunicorn processes
echo Starting Gunicorn.
exec gunicorn api:app \
    --bind 0.0.0.0:$PORT \
    --workers 3
