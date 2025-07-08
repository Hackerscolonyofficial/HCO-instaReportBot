import webbrowser
import time

def report_fake_account():
    print("\033[91m" + "=== HCO Insta Report Bot ===" + "\033[0m")
    
    username = input("\033[92mEnter the fake Instagram username (without @): \033[0m")
    reason = input("\033[92mReason for reporting (e.g., impersonation, scam): \033[0m")
    victim_profile = input("\033[92mLink to the real/victim's account (if any): \033[0m")

    print("\n\033[91mPreparing report...\033[0m")
    time.sleep(1)

    print(f"""
\033[93mReport Summary:
---------------------
🔸 Fake Username: @{username}
🔸 Reason: {reason}
🔸 Victim Profile: {victim_profile if victim_profile else 'N/A'}
🔸 Report Link: https://www.instagram.com/{username}/
\033[0m
    """)

    open_browser = input("\033[92mOpen Instagram report page now? (y/n): \033[0m").lower()
    if open_browser == 'y':
        url = f"https://www.instagram.com/{username}/"
        webbrowser.open(url)
        print("\033[91mRedirecting to Instagram...\033[0m")
    else:
        print("\033[91mReport manually later. Stay safe!\033[0m")

if __name__ == "__main__":
    report_fake_account()
