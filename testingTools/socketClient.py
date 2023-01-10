# echo-client.py
import time
import socket

HOST = "192.168.250.41"  # The server's hostname or IP address
PORT = 64000  # The port used by the server

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    #while not connected try to connect

    s.connect((HOST, PORT))
    while True:
        var = input("Enter To Fill")         
        s.sendall(b"FFFFFFFF")
        data = s.recv(1024)
        input("Enter To Remove All")         
        s.sendall(b"00000000")

print(f"Received {data!r}")

time.sleep(100)