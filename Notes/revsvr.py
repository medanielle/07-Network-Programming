import socket

def connect():
    s = socket.socket()
    s.bind(("192.168.232.148", 8080))
    s.listen(1) 
    conn, addr = s.accept()