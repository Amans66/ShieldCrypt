# Copyright © 2025 Aman Singh. All Rights Reserved.
# GitHub: https://github.com/Amans66
# LinkedIn: https://www.linkedin.com/in/aman-singh66/

from key_encryption import custom_encrypt
from key_decryption import custom_decrypt
from aes_encryption import AESEncryption
from aes_decryption import AESDecryption
import pyfiglet
from termcolor import colored

def print_banner():
    ascii_art = pyfiglet.figlet_format("ShieldCrypt")
    colored_ascii = colored(ascii_art, "cyan")
    print(colored_ascii)
    print("********************************************************")
    print("--------------------------------------------------------")

def main():
    print_banner()
    aes_enc = AESEncryption()
    aes_dec = AESDecryption()

    while True:
        print("\nTwo-Level Encryption and Decryption System")
        print("1. Encrypt Data")
        print("2. Decrypt Data")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            plaintext = input("Enter the text to encrypt: ")
            first_level_encrypted = custom_encrypt(plaintext)  # 🔹 First-level encryption
            encrypted_text = aes_enc.encrypt(first_level_encrypted)
            print(f"Encrypted Text: {encrypted_text}")

        elif choice == "2":
            encrypted_text = input("Enter the encrypted text: ")  
            first_level_decrypted = aes_dec.decrypt(encrypted_text)
            decrypted_text = custom_decrypt(first_level_decrypted)  
            print(f"Decrypted Text: {decrypted_text}")

        elif choice == "3":
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()
