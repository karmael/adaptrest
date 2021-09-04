#!/usr/bin/env bash

if [[ $PWD =~ "scripts" ]]; then
    cd ..
fi

virtualenv -p python3 venv
source venv/bin/activate
python -m pip install -r requirements.txt

cp db.sqlite3.example db.sqlite3
cp .env.example .env

python manage.py makemigrations
python manage.py migrate
