#! /usr/bin/bash
#
# Script Name: header.sh
#
# Author: S3H4N
# Date : 05.11.2021
#
# Description: This script will print header of setup. 
#              
# Run Information: This script is run automatically by the setup.
#  

# define Banner
banner ()
{
    tput setaf 2;
    tput bold;
    echo " "
    echo "            .-._   _ _ _ _ _ _ _ _ "
    echo " .-''-.__.-'00  '-' ' ' ' ' ' ' ' '-."
    echo "'.___ '    .   .--_'-' '-' '-' _'-' '._ "
    echo " V: V 'vv-'   '_   '.       .'  _..' '.'. "
    echo "   '=.____.=_.--'   :_.__.__:_   '.   : : "
    echo "          (((____.-'        '-.  /   : : "
    echo "                             (((-'\ .' / "
    echo " Aligator v1.0             _____..'  .' "
    echo " Author:S3H4N             '-._____.-' "
    tput sgr0 ;  
}

# define banner text
bannerText1 ()
{
    tput setaf 3;
    tput bold;
    echo " ========================================================="
    echo " I made this program to install most of my favourite linux" 
    echo " applications/themes easily."   
    echo " "
    echo " Only for Ubuntu based Gnome users :)"
    echo " ========================================================="
    tput sgr0;
}

banner
bannerText1
