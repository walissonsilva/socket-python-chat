import socket
import threading

HEADER = 64
PORT = 5050
SERVER = '127.0.1.1'
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = '!DISCONNECT'

NAME = input("What's your name? ")

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((SERVER, PORT))

def send_name(name):
	name = name.encode(FORMAT)

	name_length = len(name)
	send_length = str(name_length).encode(FORMAT)
	send_length += b' ' * (HEADER - len(send_length)) # completar com espaços

	client.send(send_length)
	client.send(name)

def send(msg):
	message = msg.encode(FORMAT)
	msg_length = len(msg)
	send_length = str(msg_length).encode(FORMAT)
	send_length += b' ' * (HEADER - len(send_length)) # completar com espaços
	
	client.send(send_length)
	client.send(message)

def inputMsg():
	while True:
		msg = input()
		send(msg)

def receiveMsg():
	while True:
		msg_length = client.recv(HEADER).decode(FORMAT)

		if msg_length:
			msg_length = int(msg_length)
			msg = client.recv(msg_length).decode(FORMAT)

			print(f'{msg}')

send_name(NAME)
thread = threading.Thread(target=inputMsg)
thread.start()

receiveMsg()