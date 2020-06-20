#!/bin/bash
cd /home/www/projects/avitolog/postgresql/dump/
PGPASSWORD=Umx92WS8s pg_dump -h 127.0.0.1 -U avitolog -F p -f $(date +%Y-%m-%d_%H:%M:%S).sql avitolog