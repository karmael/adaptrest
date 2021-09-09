#!/usr/bin/env bash

if [[ $PWD =~ "scripts" ]]; then
    cd ..
fi

source venv/bin/activate
export DEPLOY=local
export PORT=8000

gunicorn adaptrest.wsgi --bind :$PORT --timeout=300 --workers=2 --threads=8 --keep-alive=60
