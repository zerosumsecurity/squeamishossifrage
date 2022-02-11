#!/usr/bin/python

import socketserver
import threading
import string
from ec import *

f = open("secret", "r")
flag = f.readline().rstrip('\n')

p = int( f.readline().rstrip('\n') )
a = int( f.readline().rstrip('\n') )
b = int( f.readline().rstrip('\n') )

f.close()

E = CurveFp( p, a, b )

STEP = E.complete_point(1)	

LEET = 1337

def is_serious(guess):
	if not all(c in string.digits for c in guess):
		return False
	guess = int(guess)
	if guess<0 or guess>=p:
		return False
	return True
		  
def take_number_of_steps(number):
	n = int(number)
	Q = n*STEP
	if Q == INFINITY:
		return "the place you started"
	else:
		return Q.x() 
	
class threadedserver(socketserver.ThreadingMixIn, socketserver.TCPServer):
    	pass

class incoming(socketserver.BaseRequestHandler):
	def handle(self):
		cur_thread = threading.current_thread()

		question = b'Riddle me this, how many steps does it take to get to 1337?\n'
		self.request.send(question)

		answer = self.request.recv(1024).decode().rstrip('\n')

		if not is_serious(answer):
			response = b'Sorry but you are not even on the right road.\n'
			self.request.send(response)
			self.request.close()
		else:
			destination = take_number_of_steps(answer)
			if LEET == destination:
				response = "You have completed your journey, here is your flag:\n"
				response += flag
				response += "\n"
			else:
				response = "Nope if you take %d steps you will end up at %s\n" % ( int(answer),str(destination) )
			self.request.send(response.encode())
			self.request.close()
		return
	
      		
server = threadedserver(("0.0.0.0", 5011), incoming)
server.timeout = 4
server_thread = threading.Thread(target=server.serve_forever)
server_thread.daemon = True
server_thread.start()

server_thread.join()
