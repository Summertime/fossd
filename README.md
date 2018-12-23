# fossd

*A simple readable Fallout Shelter Save Decryptor*

## Features:

* Simple: all default values defined, ~12 lines of crypto variable definitions, ~5 lines of operating code
* Multiple Interfaces: can be used either as a module in another program, or as a CLI tool
* Compositable: designed for simple `fossd decrypt < input | modification | fossd encrypt > output` flows


## Installation

`raise NotImplementedError`


## Usage

```sh
fossd decrypt < Vault111.sav |
  jq '.vault.storage.Lunchbox += 100' |
fossd encrypt > Vault222.sav
```
