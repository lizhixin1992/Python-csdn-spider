# coding=utf-8

from socket import *
from time import ctime

print("========================TCP时间戳服务器==============================")


HOST = ""
PORT = 21567
BUFSIZE = 1024
ADDR = (HOST, PORT)


tcpSerSock = socket(AF_INET,SOCK_STREAM)
tcpSerSock.bind(ADDR)
tcpSerSock.listen(5)

while True:
    print("等待客户端的连接：")
    tcpCliSock, addr = tcpSerSock.accept()
    print("取得连接：",addr)

    while True:
        data = tcpCliSock.recv(BUFSIZE)
        if not data:
            break

        tcpCliSock.send(bytes('[%s] %s' % (ctime(), data.decode('utf-8')), 'utf-8'))

    tcpCliSock.close()

tcpSerSock.close()
