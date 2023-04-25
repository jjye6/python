import socket

HOST = "127.0.0.1" # loopback (own pc)
PORT = 65123 # > 1023 (listening port)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # socket creation # AF_INET: ip, SOCK_STREAM: tcp, SOCK_DGRAM: udp
s.bind((HOST, PORT)) # socket association (tuple)
s.listen() # port listening mode
conn, addr = s.accept() # code block (remains waiting until receives data) # conn: entry connection, addr: entry address

with conn:
    print("Connected to:", addr)
    while True:
        data = conn.recv(1024) # standard value of data # remains waiting for client message
        if not data:
            break
        conn.sendall(data)

