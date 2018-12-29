from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives.padding import PKCS7

__all__ = ["cipher"]


crypto_backend = default_backend()


password = b"UGxheWVy"
init_vector = b"tu89geji340t89u2"


kdf = PBKDF2HMAC(
    algorithm=hashes.SHA1(),
    length=32,
    salt=init_vector,
    iterations=1000,
    backend=crypto_backend,
)


cipher = Cipher(
    algorithm=algorithms.AES(kdf.derive(password)),
    mode=modes.CBC(init_vector),
    backend=crypto_backend,
)


padding = PKCS7(block_size=cipher.algorithm.block_size)
