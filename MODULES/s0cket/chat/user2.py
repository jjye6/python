import socket

HOST = "127.0.0.1"
PORT = 60000

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))

print("Connected to", HOST)

m = "text"
while m != "":
    data = s.recv(1024)
    print("user1:", data.decode("ascii"))
    m = input("").encode("ascii")
    s.sendall(m)
    print("user2:", m.decode("ascii"))