#!bin/bash
source /home/dmitriy/PycharmProjects/avitolog/venv/bin/activate
exec daphne avitolog.asgi:application