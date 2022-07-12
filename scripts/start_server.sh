#!/bin/bash

sudo cp -r /home/ubuntu/sourcecode/blog/scripts/blog /etc/nginx/sites-available/blog

sudo service gunicorn restart
sudo service nginx restart