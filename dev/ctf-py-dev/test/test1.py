# !/usr/bin/env python
# -*- coding:utf-8 -*-
from hashlib import sha256


def xor(a, b):
    result = []
    for (i, j) in zip(a, b):
        result.append(chr(ord(i) ^ ord(j)))
    return "".join(result)


def HASH(msg):
    return sha256(msg).digest()[:8]


def zjctf_encrypt(gen_keys, hahahah):
    i = 0
    d1 = hahahah[:8]
    d2 = hahahah[8:]
    for i in gen_keys:
        d1 = xor(xor(HASH(d2), i), d1)
        d1, d2 = d2, d1
    return d2 + d1


def gen_keymap(key):
    maps = []
    _ = key
    for i in range(16):
        _ = HASH(_)
        maps.append(_)
    return maps


def encrypt(key, data):
    keys = gen_keymap(key)
    return zjctf_encrypt(keys, data).encode('hex')


if __name__ == "__main__":
    result = encrypt("zzzzzjctffffffff", "This_is_the_flag")
    print(result)
# your result = 5481cd6146f1689304b2034f0a922058
