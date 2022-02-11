#!/usr/bin/python

import socketserver
import threading
import string

MODULUS = 1461501637330902918203683623790463405026757836957
COEFF_A = 894

f = open("secret", "r")
flag = f.readline().rstrip('\n')
f.close()

EXP = flag.replace('so{', '')
EXP = EXP.replace('d}', '8')
EXP = int(EXP, 16)


def multiply(A, B, D):
    ax, az = A
    bx, bz = B
    dx, dz = D
    res_x = dz*pow((ax-az)*(bx+bz) + (ax+az)*(bx-bz), 2, MODULUS)
    res_z = dx*pow((ax-az)*(bx+bz) - (ax+az)*(bx-bz), 2, MODULUS)
    return res_x % MODULUS, res_z % MODULUS

def square(P):
    x,z = P
    res_x = pow(x+z, 2, MODULUS)*pow(x-z, 2, MODULUS)
    res_z = 4*x*z*(pow(x-z, 2, MODULUS) + (COEFF_A+2)*x*z)
    return res_x % MODULUS, res_z % MODULUS

def power(base, power):
    r0 = (1, 0)
    r1 = (base,1)
    for bit in bin(power)[2:]:
        if bit == '0':
            r1 = multiply(r0, r1, (base,1))
            r0 = square(r0)
        else:
            r0 = multiply(r0, r1, (base,1))
            r1 = square(r1)
    return r0

def mul_inv(a, b):
    # Thanks, oh internet... far too lazy to write this myself
    b0 = b
    x0, x1 = 0, 1
    if b == 1: return 1
    while a > 1:
        q = a // b
        a, b = b, a%b
        x0, x1 = x1 - q * x0, x0
    if x1 < 0: x1 += b0
    return x1

def normalize(P):
    x,z = P
    return (mul_inv(z, MODULUS) * x) % MODULUS


class threadedserver(socketserver.ThreadingMixIn, socketserver.TCPServer):
    	pass

class incoming(socketserver.BaseRequestHandler):
    def is_serious(self, number):
        return all(c in string.digits for c in number)
            
    def exponentiate(self):
        buf = self.request.recv(1024).decode().rstrip('\n')
        if self.is_serious(buf):
            base = int(buf)
            result = normalize(power(base, EXP))
            message = b'Here is mine, mine is better\n'
            message += bytes(str(result), 'utf-8')
            message += b'\n'
        else:
            message = b'Bye\n'
        self.request.send(message)
        
    def handle(self):
        cur_thread = threading.current_thread()
        welcome = b'Gimme your number:\n'
        self.request.send(welcome)
        self.exponentiate()
        self.request.close()
        return 
      		
server = threadedserver(("0.0.0.0", 5114), incoming)
server.timeout = 4
server_thread = threading.Thread(target=server.serve_forever)
server_thread.daemon = True
server_thread.start()

server_thread.join()
