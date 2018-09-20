#!/bin/bash
cp /nginx.conf /etc/nginx/nginx.conf
python config_nginx.py
sleep 1
echo "daemon off;" >> /etc/nginx/nginx.conf
nginx
