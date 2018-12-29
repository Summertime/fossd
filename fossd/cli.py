import json
import sys

from . import encrypt as fossd_encrypt, decrypt as fossd_decrypt


def decrypt():
    input_data = fossd_decrypt(sys.stdin.buffer.read())  # stdin as bin
    print(json.dumps(input_data, indent=2))  # stdout as text


def encrypt():
    input_data = json.loads(sys.stdin.read())  # stdin as text
    sys.stdout.buffer.write(fossd_encrypt(input_data))  # stdout as bin
