# coding=utf-8

import socketserver
from time import ctime


print("====================SocketServer TCP服务端===================================")

HOST = ""
PORT = 21567
ADDR = (HOST, PORT)

class MyRequestHandler(socketserver.StreamRequestHandler):
    def handle(self):
        print("连接到：",self.client_address)
        while True:
            recvData = self.request.recv(1024)
            if not recvData:
                break
            print(str(recvData,'utf-8'))
            self.request.sendall(recvData)
        self.request.close()


tcpSerSock = socketserver.TCPServer(ADDR,MyRequestHandler)
print("等待连接......")
tcpSerSock.serve_forever()