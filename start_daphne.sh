#!bin/bash
source /home/dmitriy/PycharmProjects/python3.8/avitolog/venv/bin/activate
exec daphne avitolog.asgi:application