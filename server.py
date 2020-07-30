import socket
import threading

HEADER = 64
PORT = 5050
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = '!DISCONNECT'
CLIENTS = {}

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)

def handle_client(conn, addr):
	print('New connection:', addr, 'detected.')

	getName(conn)

	connected = True
	while connected:
		msg_length = conn.recv(HEADER).decode(FORMAT)

		if msg_length:
			msg_length = int(msg_length)
			msg = conn.recv(msg_length).decode(FORMAT)

			print(f'{CLIENTS[conn]} says: {msg}')

			msg = (CLIENTS[conn] + ': ' + msg).encode(FORMAT)
			msg_length = len(msg)
			send_length = str(msg_length).encode(FORMAT)
			send_length += b' ' * (HEADER - len(send_length)) # completar com espaços
			
			for client in CLIENTS.keys():
				client.send(send_length)
				client.send(msg)

	conn.close()

def getName(conn):
	msg_length = conn.recv(HEADER).decode(FORMAT)

	if msg_length:
		msg_length = int(msg_length)
		msg = conn.recv(msg_length).decode(FORMAT)

		if conn not in CLIENTS:
			CLIENTS[conn] = msg

def start():
	server.listen()
	while True:
		conn, addr = server.accept()
		thread = threading.Thread(target=handle_client, args=(conn, addr))
		thread.start()
		print('Active connections:', threading.active_count() - 1)

print('SERVER is running...')
start()