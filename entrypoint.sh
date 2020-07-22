#!/bin/sh
WORKDIR /usr/src/app/

python3 manage.py makemigrations

echo "Apply database migrations"
python3 manage.py migrate
exec "$@"