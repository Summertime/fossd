import base64
import json

from .crypto_primitives import cipher


def decrypt(save_file: bytes) -> dict:
    decryptor = cipher.decryptor()
    save_file = base64.b64decode(save_file)
    save_file = decryptor.update(save_file) + decryptor.finalize()
    save_file = save_file.strip(b"\x05")
    return json.loads(save_file)


def encrypt(json_dict: dict) -> bytes:
    raise NotImplementedError
