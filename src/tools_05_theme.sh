#! /usr/bin/bash
#
# Script Name: theme.sh
#
# Author: S3H4N
# Date : 05.11.2021
#
# Description: This script will install dracula theme, tela icon theme.
#              
# Run Information: This script is run automatically by the setup.
#                   

# create directories for themes and icons
cd ~/aligator
mkdir -p ~/.themes ~/.icons

# get dracula theme and tela icon pack
git clone https://github.com/dracula/gtk.git
git clone https://github.com/vinceliuice/Tela-icon-theme.git
git clone https://github.com/dracula/gnome-terminal

# add dracula theme to the .theme directory 
mv gtk gtk-master
cp -r gtk-master ~/.themes/

# setup dracula theme - remember to use gnome tweks to setup theme
gsettings set org.gnome.desktop.interface gtk-theme "Dracula"
gsettings set org.gnome.desktop.wm.preferences theme "Dracula"

# add tela icon theme to the .icon directory : to activate use gnome tweaks
cd Tela-icon-theme
./install.sh -d ~/.icons
cd ..

# install and setup dracula theme for terminal
cd gnome-terminal
./install.sh
cd ..

