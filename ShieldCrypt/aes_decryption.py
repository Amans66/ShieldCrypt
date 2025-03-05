# Description: Implements AES decryption to retrieve the first-level encrypted text.
from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad
import base64

AES_SECRET_KEY = b'ShieldCrypt16Key'  # 🔑 Same AES Key as used in Encryption

class AESDecryption:
    def decrypt(self, enc_data):
        """Decrypts AES encrypted data using the fixed key."""
        encrypted_bytes = base64.b64decode(enc_data)  # Decode from Base64

        cipher = AES.new(AES_SECRET_KEY, AES.MODE_ECB)
        decrypted_bytes = unpad(cipher.decrypt(encrypted_bytes), AES.block_size)

        return decrypted_bytes.decode()
