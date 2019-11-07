#!/usr/bin/env bash
# a Bash script that sets up your web servers for the deployment of web_static
sudo apt-get -y update
sudo apt-get -y install nginx
sudo mkdir -p /data/web_static/releases/test/
sudo mkdir -p /data/web_static/shared/
sudo mkdir -p /data/web_static/current/
printf "<html>\n
        <head>\n
        <body>\n
                Holberton School for the win!\n
        </body>\n
        </html>\n" > /data/web_static/releases/test/index.html
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current
sudo chown -R ubuntu:ubuntu /data/
sudo sed -i "35i location /hbnb_static {\n alias /data/web_static/current; \n}\n" /etc/nginx/sites-available/default
service nginx restart