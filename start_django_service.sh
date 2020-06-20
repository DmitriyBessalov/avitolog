#!bin/bash
cd /home/www/projects/avitolog
source ./venv/bin/activate

python3 manage.py runserver 0.0.0.0:8000
# exec daphne -b 0.0.0.0 -p 8000 avitolog.asgi:application