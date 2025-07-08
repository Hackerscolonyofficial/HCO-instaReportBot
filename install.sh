#!/data/data/com.termux/files/usr/bin/bash

# 🤖 HCO InstaReportBot Installer Script (Termux)

echo -e "\e[91m
  _    _  _____   ____       ____                      _   _       _   
 | |  | ||_   _| |  _ \     |  _ \ ___  ___ ___   ___ | |_| |_   _| |_ 
 | |  | |  | |   | |_) |____| |_) / _ \/ __/ __| / _ \| __| | | | | __|
 | |__| |  | |   |  _ <_____|  _ <  __/\__ \__ \| (_) | |_| | |_| | |_ 
  \____/   |_|   |_| \_\    |_| \_\___||___/___(_)___/ \__|_|\__,_|\__|
                                                                      
\e[0m"

echo -e "\e[93m[+] Installing HCO-InstaReportBot...\e[0m"

# Create working directory
mkdir -p $HOME/HCO-InstaReport
cd $HOME/HCO-InstaReport

# Check if obfuscated insta_report.py is in Downloads
if [ -f /sdcard/Download/insta_report.py ]; then
    cp /sdcard/Download/insta_report.py .
    echo -e "\e[92m[✓] Obfuscated script copied successfully.\e[0m"
else
    echo -e "\e[91m[!] Error: insta_report.py not found in /sdcard/Download\e[0m"
    echo -e "\e[94mPlease download it and place it in your Downloads folder first.\e[0m"
    exit 1
fi

# Run the bot
echo -e "\e[96m[>] Launching the bot...\e[0m"
python insta_report.py
