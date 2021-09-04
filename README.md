# AdaptREST

This is a simple REST API for TODO application, mini project for KM Program 2021.

## Prerequisites
1. Python 3
2. Python's Virtualenv

## Developing
1. Setup Server
```bash
virtualenv -p python3 venv
source venv/bin/activate
python -m pip install -r requirements.txt

cp db.sqlite3.example db.sqlite3
cp .env.example .env

python manage.py makemigrations
python manage.py migrate
```
or
```bash
bash scripts/setup.sh
```
2. Update environment variables (.env file)
3. Running Server (local)
```bash
source venv/bin/activate
export DEPLOY=local
export PORT=8000

python manage.py runserver 0.0.0.0:$PORT
```
or
```bash
bash scripts/run.sh
```

## Deploying
1. Refer to "Developing" section for setup process
2. Running Server (using gunicorn)
```bash
source venv/bin/activate
export DEPLOY=live
export PORT=8000

gunicorn adaptrest.wsgi --bind :$PORT --timeout=300 --workers=2 --threads=8 --keep-alive=60
```
or
```bash
bash scripts/gunicorn.sh
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
