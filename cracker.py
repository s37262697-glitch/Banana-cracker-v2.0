import os
import time
from colorama import init, Fore

# Initialize colorama
init(autoreset=True)

def show_banner():
    banner = r"""
     ____                                        ___ 
    / __ )____ _____  ____ _____  ____ _   _   _|__ \
   / __  / __ `/ __ \/ __ `/ __ \/ __ `/  | | / /_/ /
  / /_/ / /_/ / / / / /_/ / / / / /_/ /   | |/ / __/ 
 /_____/\__,_/_/ /_/\__,_/_/ /_/\__,_/    |___/____/
    """
    print(Fore.YELLOW + banner)

def get_wordlist():
    choice = input("Use default 'rockyou.txt'? (y/n): ").lower()
    
    if choice == 'y':
        path = "rockyou.txt"
    else:
        path = input("Enter the path to your wordlist: ")
    
    if not os.path.exists(path):
        print("File not found.")
        return None
    return path

def run_cracker():
    show_banner()
    
    wordlist = get_wordlist()
    if not wordlist:
        return

    print(f"Using wordlist: {wordlist}")
    
    # Example loop structure
    with open(wordlist, 'r', encoding='latin-1') as f:
        for password in f:
            password = password.strip()
            
            try:
                # Connection logic goes here
                time.sleep(1) 
                print(f"Trying: {password}")
                
            except Exception as e:
                print(f"Error encountered: {e}")
                time.sleep(2)
                continue

if __name__ == "__main__":
    run_cracker()
