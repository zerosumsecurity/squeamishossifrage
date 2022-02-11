#!/usr/bin/python

import os
import socketserver
import threading
import random
import base64
from Crypto.Cipher import AES, DES3, Blowfish, DES, ARC4
from secret import FLAG

ZERO = b'\0' * 16

while len(FLAG)%16 > 0:
	FLAG += b'.'

def encrypt(iv, key, data):
	algorithms = [
		AES.new(key, AES.MODE_ECB),
		AES.new(key, AES.MODE_CBC, iv),
		AES.new(key, AES.MODE_CFB, iv, segment_size=128),
		AES.new(key, AES.MODE_OFB, iv),
		DES3.new(key[:24], DES3.MODE_ECB),
		DES3.new(key[:24], DES3.MODE_CBC, iv[:8]),
		DES3.new(key[:24], DES3.MODE_CFB, iv[:8], segment_size=64),
		DES3.new(key[:24], DES3.MODE_OFB, iv[:8]),
		Blowfish.new(key, Blowfish.MODE_ECB),
		Blowfish.new(key, Blowfish.MODE_CBC, iv[:8]),
		Blowfish.new(key, Blowfish.MODE_CFB, iv[:8], segment_size=64),
		Blowfish.new(key, Blowfish.MODE_OFB, iv[:8]),
		DES.new(key[:8], DES.MODE_ECB),
		DES.new(key[:8], DES.MODE_CBC, iv[:8]),
		DES.new(key[:8], DES.MODE_CFB, iv[:8], segment_size=64),
		DES.new(key[:8], DES.MODE_OFB, iv[:8]),
		ARC4.new(key + iv),
	]
	return random.choice(algorithms).encrypt(data)

def encrypt_flag(iv, key):
	return iv + encrypt(iv,key,FLAG)

def update_iv(iv, key):
	return encrypt(iv, key, ZERO)
	
class threadedserver(socketserver.ThreadingMixIn, socketserver.TCPServer):
    	pass

class incoming(socketserver.BaseRequestHandler):
	def handle(self):
		cur_thread = threading.current_thread()

		key = os.urandom(32) # generate a new random key for each connection
		iv = os.urandom(16) # generate a new iv

		while True:	
			enc = encrypt_flag(iv, key)
		
			self.request.send(b"Here's the flag - securely encrypted:\n")
			self.request.send(base64.b64encode(enc)) # there you go
			self.request.send(b"\nWould you like another one? (yes/no) ")
			answer = self.request.recv(1024)
			
			if not b"yes" in answer:
				self.request.close()
				return
			else:
				iv = update_iv(iv, key) # ensure we are not reusing iv's
			
      		
server = threadedserver(("0.0.0.0", 5060), incoming)
server.timeout = 4
server_thread = threading.Thread(target=server.serve_forever)
server_thread.daemon = True
server_thread.start()

server_thread.join()
