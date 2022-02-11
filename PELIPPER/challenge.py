#!/usr/bin/python

f = open("flag.txt", "r")
flag = f.read().rstrip("}\n").lstrip("so{")
FLAG = int(flag, 16)
f.close()

MODULUS = 218109990810587981620614798421945833763
BASE = (9, 24771663703375036614544157814428100486)

def add(A, B):
    x1, y1 = A
    x2, y2 = B
    return ((x1*x2 + 4*y1*y2) % MODULUS, (x1*y2 + x2*y1 + 2*y1*y2) % MODULUS)

def mul(A, k):
    out = (1, 0)
    while k > 0:
        if k & 1:
            out = add(out, A)
        A = add(A, A)
        k >>= 1
    return out

print( mul(BASE, FLAG) )