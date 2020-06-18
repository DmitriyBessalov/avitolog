#!bin/bash
cd /home/www/projects/avitolog
source ./venv/bin/activate
exec daphne -b 0.0.0.0 -p 8000 avitolog.asgi:application