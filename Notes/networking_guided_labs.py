"""
>>> import socket
>>> host_name = socket.gethostname()
>>> pritn(host_name)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'pritn' is not defined
>>> print(host_name)
osboxes
>>> print(socket.gethostbyname(host_name))
127.0.1.1
"""
#!/usr/bin/env python

# This program is optimized for Python 2.7.12 and Python 3.5.2.
# It may run on any other version with/without modifications.
    
import socket
    
    
def print_machine_info():
    host_name = socket.gethostname()
    ip_address = socket.gethostbyname(host_name)
    print ("Host name: %s" %host_name)
    print ("IP address: %s" %ip_address)
    
#if __name__ == '__main__':
    #print_machine_info()

""" Output:
Host name: osboxes
IP address: 127.0.1.1
"""

# Retrieving a remote machine's IP address

#!/usr/bin/env python

import socket

def get_remote_machine_info():
    remote_host = 'ducks'

    try:
        print ("IP address of %s: %s" %(remote_host, socket.gethostbyname(remote_host)))
    except socket.error as err_msg:
        print ("%s: %s" %(remote_host, err_msg))

#if __name__ == '__main__':
#    get_remote_machine_info()


# Finding a service name, given the port and protocol

#!/usr/bin/env python 

 
import socket 
 
def find_service_name(): 
    protocolname = 'tcp' 
    for port in [80, 25]: 
        print ("Port: %s => service name: %s" %(port, socket.getservbyport(port, protocolname))) 
     
    print ("Port: %s => service name: %s" %(53, socket.getservbyport(53, 'udp'))) 
     
#if __name__ == '__main__': 
#    find_service_name() 


# Converting integers to and from host to network byte order

#!/usr/bin/env python 

 
import socket 
 
def convert_integer(): 
    data = 1234 
    # 32-bit 
    print ("Original: %s => Long  host byte order: %s, Network byte order: %s" %(data, socket.ntohl(data), socket.htonl(data))) 
    # 16-bit 
    print ("Original: %s => Short  host byte order: %s, Network byte order: %s" %(data, socket.ntohs(data), socket.htons(data))) 
 
     
#if __name__ == '__main__': 
#    convert_integer() 

# Modifying a socket's send/receive buffer sizes

#!/usr/bin/env python 
 
import socket 
 
SEND_BUF_SIZE = 4096 
RECV_BUF_SIZE = 4096 
 
def modify_buff_size(): 
    sock = socket.socket( socket.AF_INET, socket.SOCK_STREAM ) 
     
    # Get the size of the socket's send buffer 
    bufsize = sock.getsockopt(socket.SOL_SOCKET, socket.SO_SNDBUF) 
    print ("Buffer size [Before]:%d" %bufsize) 
     
    sock.setsockopt(socket.SOL_TCP, 
                     socket.TCP_NODELAY, 1) 
    sock.setsockopt( 
            socket.SOL_SOCKET, 
            socket.SO_SNDBUF, 
            SEND_BUF_SIZE) 
    sock.setsockopt( 
            socket.SOL_SOCKET, 
            socket.SO_RCVBUF, 
            RECV_BUF_SIZE) 
    bufsize = sock.getsockopt(socket.SOL_SOCKET, socket.SO_SNDBUF) 
    print ("Buffer size [After]:%d" %bufsize) 
 
#if __name__ == '__main__': 
#    modify_buff_size()

# Writing a simple TCP echo client/server application

import socket
import sys
import argparse

host = 'localhost'
data_payload = 2048
backlog = 5 

def echo_server(port):
    """ A simple echo server """
    # Create a TCP socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # Enable reuse address/port 
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    # Bind the socket to the port
    server_address = (host, port)
    print ("Starting up echo server  on %s port %s" % server_address)
    sock.bind(server_address)
    # Listen to clients, backlog argument specifies the max no. of queued connections
    sock.listen(backlog) 
    while True: 
        print ("Waiting to receive message from client")
        client, address = sock.accept() 
        data = client.recv(data_payload) 
        if data:
            print ("Data: %s" %data)
            client.send(data)
            print ("sent %s bytes back to %s" % (data, address))
        # end connection
        client.close() 
    
def echo_svr():
    parser = argparse.ArgumentParser(description='Socket Server Example')
    parser.add_argument('--port', action="store", dest="port", type=int, required=True)
    given_args = parser.parse_args() 
    port = given_args.port
    echo_server(port)

# echo_svr()

#!/usr/bin/env python3 

import socket 
import sys 
 
import argparse
 
host = 'localhost' 
 
def echo_client(port): 
    """ A simple echo client """ 
    # Create a TCP/IP socket 
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
    # Connect the socket to the server 
    server_address = (host, port) 
    print ("Connecting to %s port %s" % server_address) 
    sock.connect(server_address) 
     
    # Send data 
    try: 
        # Send data 
        message = "Test message. This will be echoed" 
        print ("Sending %s" % message) 
        sock.sendall(message.encode('utf-8')) 
        # Look for the response 
        amount_received = 0 
        amount_expected = len(message) 
        while amount_received < amount_expected: 
            data = sock.recv(16) 
            amount_received += len(data) 
            print ("Received: %s" % data) 
    except socket.error as e: 
        print ("Socket error: %s" %str(e)) 
    except Exception as e: 
        print ("Other exception: %s" %str(e)) 
    finally: 
        print ("Closing connection to the server") 
        sock.close() 
     
def echo_clt(): 
    parser = argparse.ArgumentParser(description='Socket Server Example') 
    parser.add_argument('--port', action="store", dest="port", type=int, required=True) 
    given_args = parser.parse_args()  
    port = given_args.port 
    echo_client(port) 

# echo_clt()

# Downloading data from an HTTP server

import argparse 
 
import urllib.request 
# Comment out the above line and uncomment the below for Python 2.7.x. 
#import urllib2 
 
REMOTE_SERVER_HOST = 'http://www.cnn.com' 
 
class HTTPClient: 
 
    def __init__(self, host): 
        self.host = host 
 
    def fetch(self): 
        response = urllib.request.urlopen(self.host) 
        # Comment out the above line and uncomment the below for Python 2.7.x. 
        #response = urllib2.urlopen(self.host) 
 
        data = response.read() 
        text = data.decode('utf-8') 
        return text 
 
def http_clt(): 
    parser = argparse.ArgumentParser(description='HTTP Client Example') 
    parser.add_argument('--host', action="store",
     dest="host",  default=REMOTE_SERVER_HOST) 
 
    given_args = parser.parse_args()  
    host = given_args.host 
    client = HTTPClient(host) 
    print (client.fetch())

#http_clt()

#Serving HTTP requests from your machine

# $ python -m SimpleHTTPServer 8080

# This will launch an HTTP web server on port 8080. You can access this web server from your browser by typing http://localhost:8080.

#!/usr/bin/env python 

# This program requires Python 3.5.2 or any later version 
# It may run on any other version with/without modifications. 
# 
# Follow the comments inline to make it run on Python 2.7.x. 
 
 
import argparse 
import sys 
 
from http.server import BaseHTTPRequestHandler, HTTPServer 
# Comment out the above line and uncomment the below for Python 2.7.x. 
#from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer 
 
DEFAULT_HOST = '127.0.0.1' 
DEFAULT_PORT = 8800 
 
 
class RequestHandler(BaseHTTPRequestHandler): 
    """ Custom request handler""" 
     
    def do_GET(self): 
        """ Handler for the GET requests """ 
        self.send_response(200) 
        self.send_header('Content-type','text/html') 
        self.end_headers() 
        # Send the message to browser 
        self.wfile.write(b"Hello from server!") 
        return 
     
 
class CustomHTTPServer(HTTPServer): 
    "A custom HTTP server" 
    def __init__(self, host, port): 
        server_address = (host, port) 
        HTTPServer.__init__(self, server_address, RequestHandler) 
         
 
def run_server(port): 
    try: 
        server= CustomHTTPServer(DEFAULT_HOST, port) 
        print ("Custom HTTP server started on port: %s" % port) 
        server.serve_forever() 
    except Exception as err: 
        print ("Error:%s" %err) 
    except KeyboardInterrupt: 
        print ("Server interrupted and is shutting down...") 
        server.socket.close() 
 
 
def http_svr(): 
    parser = argparse.ArgumentParser(description='Simple HTTP Server Example') 
    parser.add_argument('--port', action="store", dest="port", type=int, default=DEFAULT_PORT) 
    given_args = parser.parse_args()  
    port = given_args.port 
    run_server(port) 

# http_svr()

# Extracting RFC information

"""
The IETF landing page for RFCs is http://www.rfc-editor.org/rfc/, and reading through it tells us exactly what we want to know. We can access a text version of an RFC using a URL of the form http://www.rfc-editor.org/rfc/rfc741.txt. The RFC number in this case is 741. Therefore, we can get the text format of RFCs using HTTP.
"""


#!/usr/bin/env python3

import sys, urllib.request

def get_rfc():
    try:
        rfc_number = int(sys.argv[1])
    except (IndexError, ValueError):
        print('Must supply an RFC number as first argument')
        sys.exit(2)
    template = 'http://www.rfc-editor.org/rfc/rfc{}.txt'
    url = template.format(rfc_number)
    rfc_raw = urllib.request.urlopen(url).read()
    rfc = rfc_raw.decode()
    print(rfc)

# get_rfc()

# Downloading an RFC with requests

"""
Now, are going to create the same script but, instead of using urllib, we are going to use the requests module. For this, create a text file called RFC_download_requests.py:
"""

#!/usr/bin/env python3

import sys, requests

def download_requests():
    try:
        rfc_number = int(sys.argv[1])
    except (IndexError, ValueError):
        print('Must supply an RFC number as first argument')
        sys.exit(2)
    template = 'http://www.rfc-editor.org/rfc/rfc{}.txt'
    url = template.format(rfc_number)
    rfc = requests.get(url).text
    print(rfc)

# download_requests()

# Downloading an RFC with the socket module

"""
Now, we are going to create the same script but, instead of using urllib or requests, we are going to use the socket module for working at a low level. For this, create a text file called RFC_download_socket.py:
"""

#!/usr/bin/env python3

import sys, socket

def download_socket():
    try:
        rfc_number = int(sys.argv[1])
    except (IndexError, ValueError):
        print('Must supply an RFC number as first argument')
        sys.exit(2)

    host = 'www.rfc-editor.org'
    port = 80
    sock = socket.create_connection((host, port))

    req = ('GET /rfc/rfc{rfcnum}.txt HTTP/1.1\r\n'
    'Host: {host}:{port}\r\n'
    'User-Agent: Python {version}\r\n'
    'Connection: close\r\n'
    '\r\n'
    )

    req = req.format(rfcnum=rfc_number, host=host, port=port, version=sys.version_info[0])
    sock.sendall(req.encode('ascii'))
    rfc_bytes = bytearray()

    while True:
        buf = sock.recv(4096)
        if not len(buf):
            break
        rfc_bytes += buf
    rfc = rfc_bytes.decode('utf-8')
    print(rfc)

# download_socket()

