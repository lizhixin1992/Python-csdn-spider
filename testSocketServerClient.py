# coding=utf-8

from socket import *


print("=====================SocketServer TCP客户端=====================");

HOST = '127.0.0.1'
PORT = 21567
BUFSIZ = 1024
ADDR = (HOST, PORT)

tcpCliSock = socket(AF_INET, SOCK_STREAM)
tcpCliSock.connect(ADDR)

while True:
    data = input('> ')
    if not data:
        break
    tcpCliSock.send(bytes(data+'\n','utf-8'))
    buffer = tcpCliSock.recv(BUFSIZ)
    if not buffer:
        break
    print(str(buffer,'utf-8'))

tcpCliSock.close()