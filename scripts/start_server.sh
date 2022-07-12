#!/bin/bash

sudo cp -r /home/ubuntu/sourcecode/blog/scripts/blog /etc/nginx/site-available/

sudo service gunicorn restart
sudo service nginx restart