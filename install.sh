#!/bin/bash

# HCO-INSTA-BAN Install Script

echo -e "\e[91m[+] Installing HCO Insta Ban Tool...\e[0m"
sleep 1

# Update packages
pkg update -y && pkg upgrade -y

# Install dependencies
pkg install python -y
pkg install termux-api -y

# Done
echo -e "\e[92m[+] Installation Complete!\e[0m"
echo -e "\e[96m[+] Run the tool using: \e[92mpython insta_report.py\e[0m"
