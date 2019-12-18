import socket
import sys
import time

def half_clt():
    print("Welcome to python chat ")
    print("")
    print("Initiallsing....")
    time.sleep(1)

    s = socket.socket()
    print("")
    host = input(str("Please enter server adress : "))
    print("")
    name = input(str("Please enter your name : "))
    port = 8080
    print("")
    time.sleep(1)
    s.connect((host,port))
    print("Connected...")

    ## Conection done ##

    s.send(name.encode())
    s_name = s.recv(1024)
    s_name = s_name.decode()
    print("")
    print( s_name, "has joined the chat room ")

    while 1:
        message = s.recv(1024)
        message = message.decode()
        print("")
        print(name,": ",message)
        print("")
        message = input(str("Please enter your enter message : "))
        print("")
        s.send(message.encode())


def half_svr():
    import socket
    import sys
    import time

    s = socket.socket()
    host = socket.gethostname()
    port = 8080
    s.bind((host,port))
    print("")
    print("Sever adress is", host)
    print("")
    name = input(str("Please enter your username : "))
    s.listen(1)
    print("")
    print("Waiting for any incoming connections ... ")
    print("")
    conn, addr = s.accept()
    print("Recieved connection")

    #connection done ###

    s_name = conn.recv(1024)
    s_name = s_name.decode()
    print("")
    print(s_name, "has connected to the chat room")
    print("")
    conn.send(name.encode())

    ## messaging loop ##

    while 1:
        message = input(str("Please enter enter your message : "))
        print("")
        conn.send(message.encode())
        message = conn.recv(1024)
        message = message.decode()
        print("")
        print(name,": ",message)
        print("")