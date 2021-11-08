#! /usr/bin/bash
#
# Script Name: list.sh
#
# Author: S3H4N
# Date : 05.11.2021
#
# Description: This script will print package list. 
#              
# Run Information: This script is run automatically by the setup.
#  

banner01()
{
    tput bold
    echo " [Basic Tools]"
    tput sgr0
    echo "	 01. Preload      : System Boost"
    echo "	 02. Ubuntu Extras: Media Codecs-Fonts"
    echo "	 03. Gnome Tweaks : Customize Gnome DE"
    echo "	 04. Stacer       : GUI System Cleaner"
    echo "	 05. Timeshift    : Backup Service"
    echo "	 06. Alacritty    : Simple Terminal"
    echo "	 07. Tor          : Tor Service"
    echo "	 08. Synaptic     : Package Manager"
    echo "	 09. Net Tools    : Network Tools"
    echo "	 10. Wget         : Download tool"
    echo "	 11. Curl         : Download tool"
    echo "	 12. D-conf       : Configuration tool"
    echo " ----------------------------------------------------"
}

banner02()
{
    tput bold
    echo " [Programming Tools]"
    tput sgr0
    echo "	 13. GCC          : GCC Compiler for C"
    echo "	 14. Clang        : Clang for C"
    echo "	 15. Python       : Python3 and Pip3"
    echo " ----------------------------------------------------"
}

banner03()
{
    tput bold
    echo " [Web Developing Tools]"
    tput sgr0
    echo "	 16. PHP          : PHP 8.0"
    echo "	 17. Apache2      : Apache Web Server"
    echo "	 18. MySQL        : MySQL Database server"
    echo " ----------------------------------------------------"
}

banner04()
{
    tput bold
    echo " [Terminal Based Tools]"
    tput sgr0
    echo "	 19. Htop         : CLI System Monitor"
    echo "	 20. Ranger       : CLI File Manager"
    echo "	 21. Fish         : Highly Customizable Shell"
    echo "	 22. Starship     : Customizable Shell Prompt"
    echo "	 23. CMatrix      : Matrix Effect"
    echo "	 24. Figlet       : ASCII Banner Tool"
    echo "	 25. Neofetch     : Stylish System Info Tool"    
    echo " ----------------------------------------------------"
}

banner05()
{
    tput bold
    echo " [Themes]"
    tput sgr0
    echo "	 26. Dracula      : GTK Theme"
    echo "	 27. Tela         : Icon Pack"
    echo "	 28. Dracula      : Terminal-Theme"    
    echo " ----------------------------------------------------"
}

banner01
banner02
banner03
banner04
banner05
