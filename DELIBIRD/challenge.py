#!/usr/bin/python

import socketserver
import threading
import time
from secret import flag

flag = int( flag.hex(), 16 )

# sure, factor this 
n = 0xc2e5c046b514624010ea1670b19c497da80f6459bf84c76c45561e55ca97aa379ccf6191db5d8f9c9b66bd5fe288bbadf104c027638f63417256cdc90733e0b618de44c2e7420df47b488cb6ed418cd16541d659fa8e72b0d6086ede5108e5dbee86ac94962ccc3af443a4c5e9aaca61bc3816cbe2b8748e3815c71fca2415d

MODULUS = pow(2,64)

def encrypt_flag():
	e = pow(1337, int(time.time()), MODULUS)
	return pow(flag,e,n)
	
class threadedserver(socketserver.ThreadingMixIn, socketserver.TCPServer):
    	pass

class incoming(socketserver.BaseRequestHandler):
	def handle(self):
		cur_thread = threading.current_thread()
		enc = encrypt_flag() # encrypt the flag
		self.request.send( str(enc).encode('utf-8') ) # there you go	
		self.request.close()
		return		
      		
server = threadedserver(("0.0.0.0", 5225), incoming)
server.timeout = 4
server_thread = threading.Thread(target=server.serve_forever)
server_thread.daemon = True
server_thread.start()

server_thread.join()
