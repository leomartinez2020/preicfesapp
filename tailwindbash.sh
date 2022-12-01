#!/usr/bin/bash

npm run build:prod

sudo systemctl restart gunicorn
