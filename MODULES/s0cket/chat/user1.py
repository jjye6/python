import socket

HOST = "127.0.0.1"
PORT = 60000

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen()
conn, addr = s.accept()

print("Connected to", addr)

m = input("").encode("ascii")
while m != "":
    conn.sendall(m)
    print("user1:", m.decode("ascii"))
    data = conn.recv(1024)
    print("user2:", data.decode("ascii"))
    m = input("").encode("ascii")
