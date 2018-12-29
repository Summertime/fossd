# fossd

*A simple readable Fallout Shelter Save Decryptor*

## Features:

* Simple: all default values defined, ~12 lines of crypto variable definitions, ~5 lines of operating code
* Multiple Interfaces: can be used either as a module in another program, or as a CLI tool
* Compositable: designed for simple shell scripting flows


## Usage

```sh
foss-decrypt < Vault111.sav | jq '.vault.storage.Lunchbox += 100' | foss-encrypt > Vault222.sav
```

## Implementation details (for other implementations)

The data is padded to the cipher's blocksize (32?) using PKCS7

the key derivitation function is `PBKDF2HMAC`, using `SHA1`, with `1000` iterations, and an output length of `32` bytes. The salt is the bytes `tu89geji340t89u2` (ascii format)

we then derive a key using the bytes `UGxheWVy` (ascii format)

The cipher is AES (using the key prior) in CBC mode (using the bytes `tu89geji340t89u2` (ascii format) as the initial vector)
