#!/usr/bin/python

from secret import FLAG

FLAG = int( FLAG.rstrip("}\n").lstrip("so{"), 16)

# parameters

MODULUS = 148461513522929110221538679597995887283
BASE = (2,35260129722633433287870457471028337487)

def add(A, B):
    x1, y1 = A
    x2, y2 = B
    return ((x1*x2 + 2*y1*y2) % MODULUS, (x1*y2 + x2*y1 + 2*y1*y2) % MODULUS)

def mul(A, k):
    out = (1, 0)
    while k > 0:
        if k & 1:
            out = add(out, A)
        A = add(A, A)
        k >>= 1
    return out

print( mul(BASE, FLAG) )