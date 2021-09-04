# AdaptREST

This is a simple REST API for TODO application, mini project for KM Program 2021.


## Setup Server
```bash
virtualenv -p python3 venv
source venv/bin/activate
python -m pip install -r requirements.txt

cp db.sqlite3.example sb.sqlite3

python manage.py makemigrations
python manage.py migrate
```
or
```bash
bash scripts/setup.sh
```

## Running Server
```bash
source venv/bin/activate
export DEPLOY=local
export PORT=8000

python manage.py runserver 0.0.0.0:$PORT
```
or
```bash
bash run.sh
```

## Database Description
TODO

## API Endpoints Details
### Authentication
We will use Google OAuth. Ask our team for the client secret.

TODO insert endpoint, payload, etc

TODO add more endpoints


## Disclaimer
This README is guide for linux based installation. Tested on Debian 10.
