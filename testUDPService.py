# coding:utf-8


from socket import *
from time import ctime

print("===================时间戳服务器=================================")

HOST = ""
PORT = 21567
BUFSIZE = 1024
ADDR = (HOST, PORT)

udpSerSock = socket(AF_INET,SOCK_DGRAM)
udpSerSock.bind(ADDR)


while True:
    print("等待信息......")
    data, addr = udpSerSock.recvfrom(BUFSIZE)
    udpSerSock.sendto(bytes('[%s] %s' % (ctime(), data.decode('utf-8')), 'utf-8'), addr)
    print("信息：",str(data,"utf-8"))
    print("响应信息到 ",addr)

udpSerSock.close()