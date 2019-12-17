# Writing a simple UDP echo client/server application
"""
As we have developed a simple TCP server and client in the guided labs, now look at how to develop the same with UDP.
"""
# see udp_echo.py

# Modify Python Scripts

"""
Clients - update TCP (tsTclnt.py) and UDP(tcUclnt.py) clients so that the server name isn't hardcoded into the application. User specifies name/port, use defaults if either or both are missing.
"""

#!/usr/bin/env python

from socket import *
import argparse

def tcTclnt(host, port):
    BUFSIZ = 1024
    ADDR = (host, port)

    tcpCliSock = socket(AF_INET, SOCK_STREAM)
    tcpCliSock.connect(ADDR)

    while True:
        data = input('> ')
        if not data:
            break
        tcpCliSock.send(data.encode())
        data = tcpCliSock.recv(BUFSIZ)
        if not data:
            break
        print(data)

    tcpCliSock.close()

def clt_handler(): 
    parser = argparse.ArgumentParser(description='Example') 
    parser.add_argument('--port',action="store",dest="port",type=int,default=21561,required=False)
    parser.add_argument('--host',action="store",dest="host",type=str,default='127.0.0.1',required=False) 
    given_args = parser.parse_args()  
    #port = given_args.port 
    tcTclnt(given_args.host, given_args.port)

clt_handler()
"""
SERVER CODE:
#!/usr/bin/env python

from socket import *
from time import ctime

HOST = ''
PORT = 21561
BUFSIZ = 1024
ADDR = (HOST, PORT)

tcpSerSock = socket(AF_INET, SOCK_STREAM)
tcpSerSock.bind(ADDR)
tcpSerSock.listen(5)

while True:
    print('waiting for connection...')
    tcpCliSock, addr = tcpSerSock.accept()
    print('...connected from:', addr)

    while True:
        data = tcpCliSock.recv(BUFSIZ)
        if not data:
            break
        tcpCliSock.send(('[%s] %s' % (ctime(), data)).encode())

    tcpCliSock.close()
tcpSerSock.close()
"""

#!/usr/bin/env python

from socket import *

def tsUclnt(host, port):
    BUFSIZ = 1024
    ADDR = (host, port)

    udpCliSock = socket(AF_INET, SOCK_DGRAM)

    while True:
        data = input('> ')
        if not data:
            break
        udpCliSock.sendto(data.encode(), ADDR)
        data, ADDR = udpCliSock.recvfrom(BUFSIZ)
        if not data:
            break
        print(data)

    udpCliSock.close()

def udp_clt_arg(): 
    parser = argparse.ArgumentParser(description='Example') 
    parser.add_argument('--port',action="store",dest="port",type=int,default=21560,required=False)
    parser.add_argument('--host',action="store",dest="host",type=str,default='127.0.0.1',required=False) 
    given_args = parser.parse_args()  
    #port = given_args.port 
    tsUclnt(given_args.host, given_args.port)


udp_clt_arg()


"""
SERVER CODE:

#!/usr/bin/env python

from socket import *
from time import ctime

HOST = ''
PORT = 21560
BUFSIZ = 1024
ADDR = (HOST, PORT)

udpSerSock = socket(AF_INET, SOCK_DGRAM)
udpSerSock.bind(ADDR)

while True:
    print('waiting for message...')
    data, addr = udpSerSock.recvfrom(BUFSIZ)
    udpSerSock.sendto(('[%s] %s' % (ctime(), data)).encode(), addr)
    print('...received from and returned to:', addr)

udpSerSock.close()
"""


#Networking and sockets
# https://docs.python.org/3/library/socket.html#example
"""
Example
Here are four minimal example programs using the TCP/IP protocol: a server that echoes all data that it receives back (servicing only one client), and a client using it. Note that a server must perform the sequence socket(), bind(), listen(), accept() (possibly repeating the accept() to service more than one client), while a client only needs the sequence socket(), connect(). Also note that the server does not sendall()/recv() on the socket it is listening on but on the new socket returned by accept().

The first two examples support IPv4 only.
"""
def py_echo_svr():
    # Echo server program
    import socket

    HOST = ''                 # Symbolic name meaning all available interfaces
    PORT = 50007              # Arbitrary non-privileged port
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.listen(1)
        conn, addr = s.accept()
        with conn:
            print('Connected by', addr)
            while True:
                data = conn.recv(1024)
                if not data: break
                conn.sendall(data)

def py_echo_clt():
    # Echo client program
    import socket

    HOST = 'daring.cwi.nl'    # The remote host
    PORT = 50007              # The same port as used by the server
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        s.sendall(b'Hello, world')
        data = s.recv(1024)
    print('Received', repr(data))

###### ADDED OS.listdir(os.curdir) and ctime ##########
"""
Server Code:
"""
def os_time_svr():
    #!/usr/bin/env python

    from socket import *
    from time import ctime
    import os

    HOST = ''
    PORT = 21564
    BUFSIZ = 1024
    ADDR = (HOST, PORT)

    udpSerSock = socket(AF_INET, SOCK_DGRAM)
    udpSerSock.bind(ADDR)

    while True:
        print('waiting for message...')
        data, addr = udpSerSock.recvfrom(BUFSIZ)
        print('Received:', data)
        udpSerSock.sendto((f'[{ctime()}]: CWD: {os.listdir(os.curdir)} :::: Name: {os.name} ::::  Message: {data}').encode(), addr)
        #udpSerSock.sendto(('[%s] %s' % (ctime(), data)).encode(), addr)
        print('...received from and returned to:', addr)

    udpSerSock.close()

"""
Client Code:
"""
from socket import *
import os

def tsUclnt(host, port):
    BUFSIZ = 1024
    ADDR = (host, port)

    udpCliSock = socket(AF_INET, SOCK_DGRAM)

    while True:
        data = input('> ')
        if not data:
            break
        #data = data + f'From: {os.name}  :::  {os.curdir}'
        udpCliSock.sendto(data.encode(), ADDR)
        data, ADDR = udpCliSock.recvfrom(BUFSIZ)
        if not data:
            break
        print(str(data))

    udpCliSock.close()

def udp_clt_arg(): 
    parser = argparse.ArgumentParser(description='Example') 
    parser.add_argument('--port',action="store",dest="port",type=int,default=21564,required=False)
    parser.add_argument('--host',action="store",dest="host",type=str,default='127.0.0.1',required=False) 
    given_args = parser.parse_args()  
    #port = given_args.port 
    tsUclnt(given_args.host, given_args.port)


#udp_clt_arg()