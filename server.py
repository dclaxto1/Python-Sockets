# Echo server program
import socket
from datetime import *
import uuid
import os.path
import os

HOST = ''                 # Symbolic name meaning all available interfaces
PORT = 50007              # Arbitrary non-privileged port


def main():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print("Socket Created")
    s.bind((HOST, PORT))
    print("Socket binded")
    s.listen(1)
    print("Socket listened")
    myCon, myAddr = s.accept()
    print("Socket ready to connect to", myAddr)
    while (1):
        data = myCon.recv(1024)
        if not data: break
        print('LOG:', repr(data))
        if data.decode("utf8").startswith('SAY-LINE'):
            print("SAY-LINE REQUEST RECEIVED")
            msg = "'" + data.decode("utf8").split(":",1)[1] + "'"
            print(msg)
            os.system("espeak " + msg)
        if data == b'GET-MAC':
            mac = getMAC()
            myCon.sendall(mac.encode())
        if data == b'SHUTDOWN-CLIENT': break
        if data == b'SHUTDOWN-SERVER': break

#send this machines mac address
def getMAC():
    MacInt = hex(uuid.getnode()).replace('0x', '').replace('L','').upper()
    MacInt = MacInt.zfill(12)
    MacStr = '-'.join(MacInt[i:i+2] for i in range (0,11,2))
    return 'MAC' + MacStr
#run this bad boy
main()