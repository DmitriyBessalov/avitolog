FROM python:3

EXPOSE 8000

RUN
  apt-get update \
  && apt-get upgrade -y \
  && apt-get install -y supervisor \
  && useradd -d /home/www -m -s/bin/bash -c FullName,Phone,OtherInfo www
  && echo -ne "[program:daphne]"\\n \
  "command=sh /home/www/django/venv/bin/start_daphne.sh"\\n \
  "user=www"\\n \
  "process_name=daphne"\\n \
  "numproc=1"\\n \
  "autostart=1"\\n \
  "autorestart=1"\\n \
  "redirect_strerr=true" > /etc/supervisor/conf.d/daphne.conf
  && chmod +x /home/www/django/venv/bin/start_daphne.sh
  && supervisorctl reread
  && sudo supervisorctl update
  && sudo service supervisor restart
  && daphne avitolog.asgi:application