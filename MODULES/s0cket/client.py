import socket

HOST = "127.0.0.1" # server ip
PORT = 65123 # sending port

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT)) # tuple
s.sendall(b"Hello world") # in  binary

data = s.recv(1024)

print(data.decode("ascii"))