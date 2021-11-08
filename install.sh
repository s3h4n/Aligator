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

list ()
{
    # show banner
    clear
    bash src/header.sh

    # show list
    echo " "
    echo " Following Package Modules will be installed."
    echo " ----------------------------------------------------"
    bash src/list.sh
}

# confirm prompt
confirm ()
{
    while true; do
    echo " "
    echo " Following options are available,"
    echo " ----------------------------------------------------"
    echo "     * $(tput setaf 2)$(tput bold)l (list)$(tput sgr0) - Print list of installing programs"
    echo "     * $(tput setaf 2)$(tput bold)y (yes)$(tput sgr0)  - Continue to install programs"
    echo "     * $(tput setaf 2)$(tput bold)n (no)$(tput sgr0)   - Cancel the installation process"
    echo " ----------------------------------------------------"
    read -p " Please select an option : " ynl
    echo " ----------------------------------------------------"
        case $ynl in
            [Ll]* ) list;;
            [Yy]* ) break;;
            [Nn]* ) exit;;
            * ) echo " "; echo " Please answer yes-(y) or no-(n) or list-(l).";;
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

# show banner
clear
bash src/header.sh

# confirmation
confirm

# install
bash src/tools_01_basic.sh
bash src/tools_02_programming.sh
bash src/tools_03_web.sh
bash src/tools_04_cli.sh
bash src/tools_05_theme.sh

# Finals
clear
bash src/header.sh
echo " Installation successfully completed ! "
echo " "
echo " Please do these tasks after the installation."
echo "     $(tput bold)01. Install this extension to load custom themes to shell,$(tput sgr0)"
echo "            -> https://extensions.gnome.org/extension/19/user-themes/"
echo "     $(tput bold)02. Use Gnome-Tweak-Tool to Set,$(tput sgr0)"
echo "            -> Current theme to gtk-master"
echo "            -> Icon theme to Tela-Purple-Dark"
echo "            -> Shell theme to gtk-master"
echo "     $(tput bold)03. Then logout and log back to your system.$(tput sgr0)"
echo ""
echo " $(tput bold)Thank You!$(tput sgr0)"

# open gnome tweaks
gnome-tweaks

#EOF
