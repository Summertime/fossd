import base64
import json

from .crypto_primitives import cipher, padding


def decrypt(save_file: bytes) -> dict:
    decryptor = cipher.decryptor()
    unpadder = padding.unpadder()
    data = base64.b64decode(save_file)
    data = decryptor.update(data) + decryptor.finalize()
    data = unpadder.update(data) + unpadder.finalize()
    return json.loads(data.decode("utf-8"))


def encrypt(save_file: dict) -> bytes:
    data = json.dumps(save_file, separators=(",", ":")).encode("utf-8")
    encryptor = cipher.encryptor()
    padder = padding.padder()
    data = padder.update(data) + padder.finalize()
    data = encryptor.update(data) + encryptor.finalize()
    data = base64.b64encode(data)
    return data
