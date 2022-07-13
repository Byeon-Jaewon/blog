#!/bin/bash


cd /home/ubuntu/sourcecode/blog/
# sudo rm -rf /home/ubuntu/sourcecode/blog/
sudo apt-get install -y python-setuptools
sudo easy_install pip

sudo pip install -r requirement.txt