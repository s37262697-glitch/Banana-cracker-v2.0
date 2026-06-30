import os
import time
import random
from colorama import init, Fore

init(autoreset=True)

def run_cracker():
    # ... (Setup and inputs) ...
    
    # 6. Protection: Proxy Rotation
    # Rotate proxies to prevent target-side IP flagging
    current_proxy = get_random_proxy()
    
    with open(wordlist, 'r', encoding='latin-1') as f:
        for password in f:
            password = password.strip()
            time.sleep(random.uniform(1.5, 4.0)) # Jitter
            
            attempt = 0
            while attempt < 3:
                try:
                    # Logic using proxy and timeout
                    attempt_connection(target_ip, port, password, current_proxy)
                    break 
                except Exception:
                    attempt += 1
                    # 7. Protection: Rotate proxy after a failure
                    current_proxy = get_random_proxy() 
                    time.sleep(2**attempt) # Exponential Backoff

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
