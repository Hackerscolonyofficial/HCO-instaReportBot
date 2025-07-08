import os
import time
import webbrowser

def show_banner():
    os.system('clear')
    print("\033[91m" + "="*70)
    print("\033[92m" + "█░█ █▀█ █▀▀    █ █▄░█ █▀▄ ▀█▀ ▄▀█   █▄▄ ▄▀█ █▄░█")
    print("\033[92m" + "█▀█ █▄█ ██▄    █ █░▀█ █▄▀ ░█░ █▀█   █▄█ █▀█ █░▀█")
    print("\033[91m" + "="*70 + "\033[0m")
    time.sleep(1)

def show_disclaimer():
    print("\n\033[93m⚠️  This tool is not fully free.\033[0m")
    print("\033[92mTo unlock free access, support us by visiting our YouTube channel.\033[0m")
    print("\033[96m👉 LIKE 👍 | SUBSCRIBE 🔔 | Click the BELL icon\033[0m")
    input("\n\033[94mPress ENTER to continue and open YouTube...\033[0m")
    
    # Open your official YouTube channel
    youtube_link = "https://www.youtube.com/@HackersColonyTech"
    webbrowser.open(youtube_link)
    
    input("\n\033[92mAfter subscribing, press ENTER to start using the tool...\033[0m")
    os.system('clear')

def report_fake_account():
    show_banner()
    show_disclaimer()

    print("\033[92m=== Start Reporting ===\033[0m")
    username = input("\033[92mEnter the fake Instagram username (without @): \033[0m")
    reason = input("\033[92mReason for reporting (e.g., impersonation, scam): \033[0m")
    victim_profile = input("\033[92mLink to the real/victim's account (if any): \033[0m")

    print("\n\033[91mPreparing report...\033[0m")
    time.sleep(1)

    print(f"""
\033[93m📄 Report Summary
--------------------------
🔸 Fake Username: @{username}
🔸 Reason: {reason}
🔸 Victim Profile: {victim_profile if victim_profile else 'N/A'}
🔸 Report Link: https://www.instagram.com/{username}/
\033[0m
    """)

    open_browser = input("\033[92mOpen Instagram report page now? (y/n): \033[0m").lower()
    if open_browser == 'y':
        webbrowser.open(f"https://www.instagram.com/{username}/")
        print("\033[91mRedirecting to Instagram...\033[0m")
    else:
        print("\033[91mOkay. Report it manually later.\033[0m")

if __name__ == "__main__":
    report_fake_account()
