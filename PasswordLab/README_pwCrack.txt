Password Cracker (SHA-256 Dictionary Attack)
This Python project demonstrates a basic dictionary attack to crack a SHA-256 hashed password. It's intended for educational use to better understand password security and ethical hacking techniques.

How It Works
target_hash.txt contains the SHA-256 hash of the password to crack.

wordlist.txt includes possible password guesses.

The script reads each word, hashes it, and checks for a match.

How to Use
Make sure all files are in the same directory.

Open a terminal and navigate to the folder.

Run the script:

bash
Copy
Edit
python password_cracker.py
If a match is found, the plaintext password will be displayed.

