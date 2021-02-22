from socket import *

def socket_client_tcp(host, port):
	socket_client_tcp = socket(AF_INET, SOCK_STREAM)
	socket_client_tcp.connect((host, port))
	print('Conectado com : ', host, port)
	socket_client_tcp.send(b'E essa aula ai, boa?')
	data = socket_client_tcp.recv(1024)
	print('Received', repr(data))

#EC2 Machine IP
socket_client_tcp('35.153.194.255', 3333)
#socket_client_tcp("127.0.0.1", 6500)
#socket_client_tcp("192.168.56.104", 6500)