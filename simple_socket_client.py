import socket

def socket_client_tcp(host, port):
	socket_client_tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	socket_client_tcp.bind((host, port))
	print('Conectado com : ', host, port)
	socket_client_tcp.send(b'E essa aula ai, boa?')
	data = socket_client_tcp.recv(1024)
	print('Received', repr(data))

#EC2 Machine IP
socket_client_tcp('35.153.194.255', 65001)