# Create image ubuntu_python:lates
FROM ubuntu

RUN apt-get update
RUN apt-get upgrade -y
RUN apt-get install -y daphne libpq-dev python3