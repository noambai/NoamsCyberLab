import hashlib

# Load the target hash
with open("target_hash.txt", "r") as f:
    target_hash = f.read().strip()

# Load the wordlist
with open("wordlist.txt", "r") as f:
    passwords = f.readlines()

# Try each password
for password in passwords:
    password = password.strip()
    hashed_password = hashlib.sha256(password.encode()).hexdigest()
    if hashed_password == target_hash:
        print(f"[+] Password found: {password}")
        break
else:
    print("[-] Password not found in wordlist.")
