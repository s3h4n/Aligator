#! /usr/bin/bash
#
# Script Name: tools_programming.sh
#
# Author: S3H4N
# Date : 05.11.2021
#
# Description: This script will install some basic tools/application.
#              
# Run Information: This script is run automatically by the setup.
#                   

# install
sudo apt -y install preload ubuntu-restricted-extras gnome-tweak-tool stacer timeshift cargo tor synaptic net-tools wget curl dconf-cli
cargo install alacritty

cd ~/aligator
cd config
cp -r alacritty.yml ~/.config/alacritty/
cd ..