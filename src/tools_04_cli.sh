#! /usr/bin/bash
#
# Script Name: tools_programming.sh
#
# Author: S3H4N
# Date : 05.11.2021
#
# Description: This script will install command
#              line interface tools. 
#              
# Run Information: This script is run automatically by the setup.
#                   

# install c-matrix, htop Resource manager, ranger file manager, fish shell and starship 
sudo apt -y install cmatrix figlet neofetch htop ranger fish 
sh -c "$(curl -fsSL https://starship.rs/install.sh)"

# set fish shell as default shell 
chsh -s /usr/bin/fish

# setup starship prompt with fish
cd 
cd ~/aligator
cd config
cp -r fish.config ~/.config/fish/
cp -r starship.toml ~/.config/
