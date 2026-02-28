import subprocess
import socket
import sys
import datetime
import os
import time

LOG_DIR = "logs"
if not os.path.exists(LOG_DIR):
    os.makedirs(LOG_DIR)

def run_surgical_scan(target):
    print(f"\n[*] Target Locked: {target} | Initializing Ghost Protocol...")
    time.sleep(1) # Subtle pause for effect
    
    cmd = ["nmap", "-sT", "-Pn", "--top-ports", "10", "-v", target]
    full_output = ""
    
    try:
        process = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
        for line in process.stdout:
            print(f"  [WRAITH] > {line.strip()}")
            full_output += line
            
        process.wait()
        
        # The subtle "Kaboom"
        print("\n" + "-"*40)
        print("💥 KABOOM! Scan complete. Data extracted.")
        print("-"*40)
        
        timestamp = datetime.datetime.now().strftime("%H%M%S")
        log_file = f"{LOG_DIR}/strike_{target}_{timestamp}.txt"
        with open(log_file, "w") as f:
            f.write(full_output)
            
        print(f"[✔] Evidence stashed: {log_file}")
            
    except KeyboardInterrupt:
        print("\n[!] Connection Severed. Going dark...")
        sys.exit(0)

def main():
    os.system("clear")
    print(" WRAITH-SCANNER v1.1")
    print("-----------------------------------------")
    print("[1] Launch Surgical Strike")
    print("[2] Venom-Vault (STAGING - KEEP OUT)")
    
    choice = input("\nSelect Vector > ")

    if choice == '1':
        target = input("Enter Target IP: ")
        run_surgical_scan(target)
    elif choice == '2':
        print("\n[!] ACCESS DENIED. (just kidding)")
        print("[!] Venom-Vault is in 48-hour development.")

if __name__ == "__main__":
    main()

