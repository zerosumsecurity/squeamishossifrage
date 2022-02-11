from hashlib import md5
import socketserver
import threading
import string
import hmac


PRE_ENVELOPE = b'so{'
POST_ENVELOPE = b'}'

f = open("secret", "r")
SECRET = f.readline().rstrip('\n')
f.close()

AUTH_KEY = bytes(SECRET, 'utf-8')
FLAG = PRE_ENVELOPE + AUTH_KEY + POST_ENVELOPE

def hash(data):
    return hmac.new(data, AUTH_KEY, md5).digest()
    
def check_format(flag):
    res = True
    if flag[:3] != PRE_ENVELOPE or flag[-1:] != POST_ENVELOPE:
        res = False 
    return res

def verify(flag1, flag2):
    if not check_format(flag1):
        return False
    if not check_format(flag2):
        return False
    if flag1 == flag2:
        return False
    if hash(flag1) == hash(flag2):
        return True
    else:
        return False

class threadedserver(socketserver.ThreadingMixIn, socketserver.TCPServer):
    	pass

class incoming(socketserver.BaseRequestHandler):
    def handle(self):
        cur_thread = threading.current_thread()

        offer = b'Please give me your first flag:\n'
        self.request.send(offer)        
        flag1 = self.request.recv(1024)
        
        offer = b'Please give me your second flag:\n'
        self.request.send(offer)
        flag2 = self.request.recv(1024)

        if verify(flag1, flag2):
            response = b'Congratulations, here is your fresh flag:\n'
            response += FLAG
            response += b'\n'
        else:
            response = b'Nope\n'
        
        self.request.send(response)
        self.request.close()
        return
      		
server = threadedserver(("0.0.0.0", 5132), incoming)
server.timeout = 4
server_thread = threading.Thread(target=server.serve_forever)
server_thread.daemon = True
server_thread.start()

server_thread.join()
