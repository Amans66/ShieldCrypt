# Description: Implements AES encryption for the second level of encryption.
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
import base64

AES_SECRET_KEY = b'ShieldCrypt16Key'  # 🔑 Fixed 16-byte AES Key

class AESEncryption:
    def encrypt(self, data):
        """Encrypts data using AES and stores the AES key in a fixed manner."""
        cipher = AES.new(AES_SECRET_KEY, AES.MODE_ECB)
        padded_data = pad(data.encode(), AES.block_size)
        encrypted_bytes = cipher.encrypt(padded_data)

        # Encode encrypted data as Base64
        return base64.b64encode(encrypted_bytes).decode()
