import json
import sys

import click

from . import encrypt as fossd_encrypt, decrypt as fossd_decrypt


@click.group()
def cli():
    ...


@cli.command()
def decrypt():
    input_data = fossd_decrypt(sys.stdin.buffer.read())
    print(json.dumps(input_data, indent=2))
