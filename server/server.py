from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import FTPServer

authorizer = DummyAuthorizer()
authorizer.add_user("jesiel", "senha123", r"C:\Users\dev\Desktop\ftp-app", "elradrmw")

handler = FTPHandler
handler.authorizer = authorizer

with FTPServer(("192.168.1.12", 21), handler) as server:
	server.max_cons = 5
	server.max_cons_per_ip = 5
	server.serve_forever()