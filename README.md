# ShieldCrypt – Advanced Two-Level Encryption Tool 🔒
Author: Aman Singh
GitHub: Amans66
LinkedIn: Aman Singh
Description: ShieldCrypt is a powerful two-layer encryption tool designed for securing sensitive data using a hybrid encryption approach. It first applies a custom encryption method (ROT13 + character substitution) and then encrypts the result using AES-128 encryption. This ensures double protection for your data.
How is ShieldCrypt Helpful?
🔹 Enhanced Security: Using two levels of encryption ensures added protection against brute-force attacks.
🔹 Data Protection: Helps secure confidential text-based information like passwords, messages, or API keys.
🔹 Privacy & Anonymity: Prevents unauthorized users from accessing encrypted data.
🔹 Lightweight & Fast: Simple Python-based encryption with minimal system resource usage.
🔹 Offline Encryption: Works without an internet connection, making it ideal for secure offline data storage.

Where Can ShieldCrypt Be Used?
✔ Personal Data Security: Encrypt personal notes, passwords, or sensitive files.
✔ Cybersecurity & Ethical Hacking: Learn about encryption techniques for cybersecurity research.
✔ Secure Communication: Encrypt messages before sharing via email or text.
✔ Cloud Storage Protection: Encrypt files before uploading to Google Drive, Dropbox, or other cloud services.
✔ CTF & Security Challenges: Can be used in Capture The Flag (CTF) competitions to encrypt/decrypt challenges.
✔ Developers & IT Security: Helps developers understand encryption for building more secure applications.

# Installation & Usage

# Step 1: Install Required Dependencies
Before running ShieldCrypt, install the necessary Python modules:

# bash
sudo apt update && sudo apt install python3 python3-pip -y
pip install pyfiglet termcolor pycryptodome

# Step 2: Clone the Repository
# bash
git clone https://github.com/Amans66/ShieldCrypt.git

cd ShieldCrypt

# Step 3: Run ShieldCrypt
# bash
python3 ShieldCrypt.py


# How It Works
1️⃣ First-Level Encryption:

Uses a custom ROT13-based encryption with symbol substitution to scramble input text.
2️⃣ Second-Level Encryption:
Encrypts the scrambled text using AES-128 encryption for added security.
3️⃣ Decryption Process:
The AES decryption is applied first, followed by reversing the custom encryption.

# Example Usage
Encrypting Data

pgsql
Enter the text to encrypt: Hello123
Encrypted Text: Uy55Nlg6a+JFA34vMw==

Decrypting Data
pgsql

Enter the encrypted text: Uy55Nlg6a+JFA34vMw==
Decrypted Text: Hello123

# Disclaimer
🚨 ShieldCrypt is for educational and research purposes only.
Do not use it for illegal activities. The author is not responsible for misuse.
