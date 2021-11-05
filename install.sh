#! /usr/bin/bash
#
# Script Name: install.sh (Aligator Setup File)
#
# Author: S3H4N
# Date : 05.11.2021
#
# Description: This script will install web development tools. 
#              
# Run Information: This script is run automatically by the setup.
#

# confirm prompt
confirm()
{
    while true; do
    read -p " Do you wish to install these programs? y or n: " yn
        case $yn in
            [Yy]* ) break;;
            [Nn]* ) exit;;
            * ) echo " Please answer yes or no.";;
        esac
    done
}

# print update-upgrade system
clear
echo " Updating the system before istalling tools."
echo " "

# update-upgrade system
sudo apt -y update
sudo apt -y install software-properties-common 
sudo apt -y upgrade

# show banner
clear
bash src/header.sh

# show list
echo " Following Package Modules will be installed."
echo " ----------------------------------------------------"
bash src/list.sh

# confirmation
confirm

# install
bash src/tools_01_basic.sh
bash src/tools_02_programming.sh
bash src/tools_03_web.sh
bash src/tools_04_cli.sh
bash src/tools_05_theme.sh

clear
bash src/header.sh
echo "Done ! (Please setup theme and the icon pack in tweak-tool.)"

#EOF
