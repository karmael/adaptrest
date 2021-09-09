#!/usr/bin/env bash

if [[ $PWD =~ "scripts" ]]; then
    cd ..
fi

source venv/bin/activate
export DEPLOY=local
export PORT=8000

python manage.py runserver 127.0.0.1:$PORT
