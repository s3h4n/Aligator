#! /usr/bin/bash
#
# Script Name: tools_programming.sh
#
# Author: S3H4N
# Date : 05.11.2021
#
# Description: This script will install web development tools. 
#              
# Run Information: This script is run automatically by the setup.
#                   

# add php 8.0 repository
sudo add-apt-repository ppa:ondrej/php

# install apache2 server, mysql, php 8.0
sudo apt update
sudo apt -y install apache2 mysql-server php8.0 libapache2-mod-php8.0 php-mysql  

# enable apache2 at start
sudo systemctl start apache2
sudo systemctl enable apache2
