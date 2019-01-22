!#/bin/sh

echo 'Waiting for postgres to start ...'
while ! nc -z users-db 5432; do
    sleep 0.1
echo 'Postgres started'

python manage.py run -h 0.0.0.0