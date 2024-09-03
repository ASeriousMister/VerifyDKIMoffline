#!/bin/bash

RED='\033[91m'
YELLOW='\033[93m'
GREEN='\033[92m'
CYAN='\033[94m'
NC='\e[0m' # No Color

sudo apt update
sudo apt install python3-pip python3-virtualenv
#sudo rm /usr/lib/python3.11/EXTERNALLY-MANAGED
virtualenv dkve
source dkve/bin/activate
pip3 install dkimpy
echo -e "$YELLOW If you encountered some pip problems stop this script with$CYAN Ctrl+C$YELLOW, disable the virtual environment typing$CYAN deactivate$YELLOW and uncomment line 5 in this script (delete #)$NC"
read -p -e "$YELLOW If everything seems to be OK, just hit$CYAN Enter$YELLOW to continue$NC"
cp -p dnsplug.py dkve/lib/python3.*/site-packages/dkim/
echo -e "$GREEN Now you can enable the virtual environment with$CYAN source dkve/bin/activate$GREEN and run$CYAN python3 verifydkim_GUI.py$GREEN to choose files for the verification or$CYAN python3 verifydkim_cli.py$GREEN using options$RED -e$GREEN to add .eml file and$RED -k$GREEN to add the dkimkey$NC"
