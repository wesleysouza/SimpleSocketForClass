import socket

def socket_client_tcp(host, port):
	socket_client_tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	socket_client_tcp.bind((host, port))
	print('Conectado com : ', host, port)
	socket_client_tcp.send(b'E essa aula ai, boa?')
	data = socket_client_tcp.recv(1024)
	print('Received', repr(data))

#Se conectando com o servidor
socket_client_tcp('127.0.0.1', 50007)