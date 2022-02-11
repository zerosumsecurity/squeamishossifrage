#!/usr/bin/env python2
# -*- coding: utf-8 -*-

import os
from pydes import des
import base64

f = open("key", "rb")
KEY = f.read()
f.close()

def pad(s):
    c = int(8 - len(s)%8).to_bytes(1, byteorder='big')
    return s + (8 - len(s) % 8) *c


def cbc_encrypt(plain):
    enc = des()
    enc.setkey(KEY)
    
    iv = os.urandom(8)
    plain = pad(plain)
    print(plain, len(plain))

    blocks = [plain[i:i+8] for i in range(0, len(plain), 8)]

    ct = iv
    for block in blocks:
        pt = bytes([a ^ b for a,b in zip(iv,block)])
        iv = enc.encrypt_block(pt)
        ct += iv 
    return ct

def encrypt_flag(flag):
    return  str(base64.standard_b64encode( cbc_encrypt(flag) ), 'utf-8')