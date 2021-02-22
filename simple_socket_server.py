import socket

def socket_server_tcp(host, port):
	socket_server_tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	socket_server_tcp.bind((host, port))
	socket_server_tcp.listen(1)
	conn, addr = socket_server_tcp.accept()
	print('NEW SOCKET', conn)
	print('Connected by', addr)
	while True:
		data = conn.recv(1024)
		if not data:
			break
		else:
			print("Dados redebidos!!")
			print(data)
			conn.send(data)

#EC2 machine port 65001
socket_server_tcp("", 65001)
