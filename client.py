# Echo client program
import socket
import uuid
import os.path
import os

HOST = 'localhost'    # The remote host
PORT = 50007              # The same port as used by the server

def main():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print("socket created")
    s.connect((HOST, PORT))
    print("socket connected")
    s.sendall(b'Hello, world')
    print("socket data sent")
    print(getMenu())
    option = input('Select: ')
    while (1):
        if option == '1':
            print('Shutting Down Client')
            s.sendall(b'SHUTDOWN-CLIENT')
            break
        elif option == '2':
            print('Shutting Down Server')
            s.sendall(b'SHUTDOWN-SERVER')
        elif option == '3':
            print('Retrieving MAC')
            s.sendall(b'GET-MAC')
            mac = s.recv(1024).decode('utf8')
            print(mac)
        elif option == '4':
            print("What do you want to speak?")
            msg = input("MSG=")
            s.sendall(b"SAY-LINE" + msg.encode())
        elif option == 'q' or option == 'Q':
            break
        print(getMenu())
        option = input('Selection or (Q)uit: ')
    print('AS-Socket-CLOSING')
    s.close()

def getMenu():
    msg = '\n\nAS - Console\n'
    msg += '1) Shutdown Client \n2) Shutdown Server \n'
    msg += '3) Report MAC \n4) Say Line'
    return msg

#run this thing
main()

        


        

