# Hashing Password

### Tech Stack:
+ Python

### Libraries used:
+ hashlib
+ argparse

###  Pre-requirements:
+ Run `pip install -r requirements.txt`

### To execute the project:
+ Run `python hashing_passwords.py`

### How to execute/ Example:
syntax: `python hashing_passwords.py <password> [-t {sha256,sha512,md5}] `
```
$ python hashing_passwords.py nakao
< hash-type : sha256 >
63201414e0804bdc63b662bd87f0f51616ab69bd672aefe2b17fcec1ef14a995
```

```
$ python hashing_passwords.py nakao -t sha512
< hash-type : sha512 >
9cae3a2096c33b6049502ac923baff9649478df62eb090bac30d5c684b2f724ecaf7c3d7744ebccb49118d2ab07d615b02a7d170fd6310f815da18e09863841a
```
