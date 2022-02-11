#! /usr/bin/env python

from BSecure import *
from Crypto.Cipher import AES

f = open("flag", "r")
flag = f.read()
f.close()

rng = BSecure_rng()

iv  = rng.get_random(16)
key = rng.get_random(32)

aes = AES.new(key, AES.MODE_CFB, iv)

f = open("flag.encrypted", "wb")
f.write( iv + aes.encrypt(flag) )
f.close()

